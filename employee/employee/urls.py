from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls')),
    # path('saml/', include('saml_auth.urls')),
    path('sso/saml/', include('saml_auth.urls')),  # ✅ This line is crucial
]
