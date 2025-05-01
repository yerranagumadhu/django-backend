from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from .saml_settings import get_saml_settings
from django.contrib.auth import login, get_user_model

def prepare_django_request(request):
    return {
        'http_host': request.get_host(),
        'script_name': request.path_info,
        'server_port': request.META.get('SERVER_PORT', '8000'),
        'get_data': request.GET.copy(),
        'post_data': request.POST.copy()
    }

def init_saml_auth(request):
    req = prepare_django_request(request)
    return OneLogin_Saml2_Auth(req, get_saml_settings())

def sso_login(request):
    auth = init_saml_auth(request)
    return redirect(auth.login())

@csrf_exempt
def acs_view(request):
    auth = init_saml_auth(request)
    auth.process_response()
    errors = auth.get_errors()

    if not errors:
        email = auth.get_nameid()
        User = get_user_model()
        user, _ = User.objects.get_or_create(username=email, defaults={'email': email})
        login(request, user)
        return redirect('/employee/')
    else:
        return render(request, 'saml_auth/login_error.html', {'errors': errors})

def sso_logout(request):
    auth = init_saml_auth(request)
    return redirect(auth.logout())

def metadata_view(request):
    from onelogin.saml2.metadata import OneLogin_Saml2_Metadata
    metadata = OneLogin_Saml2_Metadata.builder(get_saml_settings()['sp'], get_saml_settings()['idp'])
    return HttpResponse(metadata, content_type="text/xml")
