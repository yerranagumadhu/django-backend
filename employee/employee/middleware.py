from django.shortcuts import redirect

EXEMPT_URLS = ['/saml/login/', '/saml/acs/', '/saml/metadata/', '/admin/']

class SAMLLoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/emp/') and not request.user.is_authenticated:
            if request.path not in EXEMPT_URLS:
                return redirect('/saml/login/')
        return self.get_response(request)
