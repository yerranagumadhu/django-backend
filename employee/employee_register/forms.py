from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'department', 'salary', 'hire_date']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'department': 'Department',
            'salary': 'Salary',
            'hire_date': 'Hire Date',
        }