# employee_register/middleware.py
from django.shortcuts import redirect
from django.conf import settings

EXEMPT_URLS = [
    '/sso/saml/login/',
    '/sso/saml/acs/',
    '/sso/saml/metadata/',
    '/sso/saml/logout/',
    '/admin/',
    '/static/',
]


class SAMLLoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path.startswith('/employee/'):
            return redirect('/sso/saml/login/')
        return self.get_response(request)
