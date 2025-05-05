from django.shortcuts import render, redirect
from .models import Employee
from django.http import JsonResponse
from .forms import EmployeeForm # Import the EmployeeForm if you want to use it in your views
from .serializers import EmployeeDetailSerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

# Create your views here.
# List all the employees in the database

def employee_list(request):
    
    employees = Employee.objects.all()
    print(f"Number of employees fetched: {employees.count()}")
    # if not employees:
    #     print("No employees found in the database.")
    # else:
    #     print(f"Employees: {[employee.first_name for employee in employees]}")
    return render(request, "employee_register/employee_list.html", {'employees': employees})
    # return JsonResponse(
    #     {'employees': list(employees.values())},
    #     safe=False
    # )
    
# # Insert the new member into the database
# def employee_insert(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         department = request.POST.get('department')
#         salary = request.POST.get('salary')
#         hire_date = request.POST.get('hire_date')

#         employee = Employee(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             phone=phone,
#             department=department,
#             salary=salary,
#             hire_date=hire_date
#         )
#         employee.save()

#         return JsonResponse({'message': 'Employee added successfully!'}, status=201)

#     return JsonResponse({'error': 'Invalid request method.'}, status=400)

# Insert the new member into the database
def employee_insert(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_list')  # Redirect to the employee list after successful insertion
            # return JsonResponse({'message': 'Employee added successfully!', 'employee_id': employee.id}, status=201)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        # If the request method is not POST, render the form for employee creation
        form = EmployeeForm()
        return render(request, "employee_register/employee_form.html", {'form': form})

    # return JsonResponse({'error': 'Invalid request method.'}, status=400)
    # return render(request, "employee_register/employee_form.html", {'form': EmployeeForm()})

# Update the employee details
def employee_update(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found.'}, status=404)

    if request.method == 'POST':
        employee.first_name = request.POST.get('first_name', employee.first_name)
        employee.last_name = request.POST.get('last_name', employee.last_name)
        employee.email = request.POST.get('email', employee.email)
        employee.phone = request.POST.get('phone', employee.phone)
        employee.department = request.POST.get('department', employee.department)
        employee.salary = request.POST.get('salary', employee.salary)
        employee.hire_date = request.POST.get('hire_date', employee.hire_date)

        employee.save()
        
        # return JsonResponse({'message': 'Employee updated successfully!'}, status=200)
        return redirect('employee_list')
    else:
        # If the request method is not POST, render the form for employee update
        form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_updateform.html", {'form': form, 'employee_id': employee_id})
    

    # return JsonResponse({'error': 'Invalid request method.'}, status=400)

# Delete the employee from the database
def employee_delete(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found.'}, status=404)

    if request.method == 'DELETE':
        employee.delete()
        # return JsonResponse({'message': 'Employee deleted successfully!'}, status=204)
        return redirect('employee_list')
    else:
        # If the request method is not DELETE, return an error response
        # return JsonResponse({'error': 'Invalid request method. Use DELETE to remove an employee.'}, status=405) 
        return render(request, "employee_register/employee_delete.html", {'employee': employee})

    # return JsonResponse({'error': 'Invalid request method.'}, status=400)
    
# Employee Detail View
class EmployeeDetailAPIView(APIView):
    def get(self, request, employee_id):
        try:
            employee = Employee.objects.get(id=employee_id)
            serializer = EmployeeDetailSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found.'}, status=status.HTTP_404_NOT_FOUND)
        
def logout_page(request):
    return render(request, 'employee_register/logout_page.html')



@api_view(['GET'])
def employee_list_api(request):
    employees = Employee.objects.all()
    print(f"Number of employees fetched: {employees.count()}")
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

# class EmployeeListAPIView(APIView):
#     def get(self, request):
#         try:
#             employees = Employee.objects.all()
#             print(f"Number of employees fetched: {employees.count()}")
#             serializer = EmployeeSerializer(employees, many=True)
#             return Response(serializer.data)
#         except Employee.DoesNotExist:
#             return Response({'error': 'Employee not found.'}, status=status.HTTP_404_NOT_FOUND)
