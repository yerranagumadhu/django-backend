from django.urls import path
from . import views

urlpatterns = [
    path('', views.acs_view, name='saml_login'),
    path('login/', views.sso_login, name='saml_login'),
    path('acs/', views.acs_view, name='saml_acs'),    
    path('logout/', views.sso_logout, name='saml_logout'),
    path('metadata/', views.metadata_view, name='saml_metadata'),
    path('check-auth/', views.check_auth, name='check_auth'),
    
]
