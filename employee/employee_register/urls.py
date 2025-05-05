from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee'),    
    path('list/', views.employee_list, name='employee_list'),
    path('api/list/', views.employee_list_api, name='employee_list_api'),
    path('insert/', views.employee_insert, name='employee_insert'),
    path('update/<int:employee_id>/', views.employee_update, name='employee_update'),   
    path('delete/<int:employee_id>/', views.employee_delete, name='employee_delete'),
    path('api/<int:employee_id>/', views.EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('logout_page/', views.logout_page, name='logout_page'),    
]   
