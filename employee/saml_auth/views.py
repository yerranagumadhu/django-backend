from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from .saml_settings import get_saml_settings
from django.contrib.auth import login, get_user_model, logout
from django.urls import reverse
from django.http import JsonResponse

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
    if request.user.is_authenticated:
        # Already logged in, stay on the current page
        return redirect(request.GET.get('next', '/'))  # or use request.path
    auth = init_saml_auth(request)
    saml_request_url = auth.login()

    # Properly pass RelayState to auth.login()
    relay_state = request.GET.get("RelayState", "http://localhost:3000")
    return redirect(auth.login(return_to=relay_state))

@csrf_exempt
def acs_view(request):
    auth = init_saml_auth(request)
    auth.process_response()
    errors = auth.get_errors()

    if not errors:
        email = auth.get_nameid()
        User = get_user_model()
        user, _ = User.objects.get_or_create(username=email, defaults={'email': email})
        attributes = auth.get_attributes()
        authemail = attributes.get('email', [None])[0]
        first_name = attributes.get('firstName', [None])[0]
        last_name = attributes.get('lastName', [None])[0]
        print(f"Attributes received: {attributes}")
        if authemail and first_name and last_name:
            user.email = authemail
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        else:
            print("Missing required attributes from SAML response.")
        
        # Log the user in
        login(request, user)

        # Get RelayState URL from the request or fallback to 'next' if missing
        relay_state = request.POST.get('RelayState')  # This will always contain the original URL from the React app
        print(f"RelayState received: {relay_state}")
        if not relay_state:
            relay_state = request.GET.get('next', '/employee/')  # fallback URL if no RelayState or next param
        
        # Redirect to the RelayState URL (employee details page) or fallback
        return redirect(relay_state)
    else:
        # Handle SAML errors if any
        return render(request, 'saml_auth/login_error.html', {'errors': errors})
    
    
def sso_logout(request):
    
    auth = init_saml_auth(request)
    # Perform the logout and get the logout URL
    logout_url = auth.logout()    
    print(f"Logout URL: {logout_url}")
    # If a URL is returned, we can redirect the user to Okta's SSO logout endpoint
    # if logout_url:
    #     return redirect(logout_url)
    
    # If no URL is returned (or after logging out), redirect to the home page
    return redirect('logout_page')# Or any page you want after logout

def metadata_view(request):
    from onelogin.saml2.metadata import OneLogin_Saml2_Metadata
    metadata = OneLogin_Saml2_Metadata.builder(get_saml_settings()['sp'], get_saml_settings()['idp'])
    return HttpResponse(metadata, content_type="text/xml")



def check_auth(request):
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True, 'username': request.user.username})
    else:
        return JsonResponse({'authenticated': False}, status=401)