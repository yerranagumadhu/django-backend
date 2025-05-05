# Employee registration serializer
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'location']

class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ['title', 'description']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = ['score', 'comments']

class EmployeeDetailSerializer(serializers.ModelSerializer):
    # department = DepartmentSerializer()
    department = serializers.SerializerMethodField()
    job_title = JobTitleSerializer()
    projects = ProjectSerializer(many=True, read_only=True)
    performance_reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'department', 'job_title', 'salary', 'hire_date', 'projects', 'performance_reviews']

    def get_department(self, obj):
        return DepartmentSerializer(obj.department_0).data

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # or list specific fields like ['id', 'first_name', 'last_name', ...]