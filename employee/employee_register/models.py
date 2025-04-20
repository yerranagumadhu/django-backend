from django.db import models


class Attendance(models.Model):
    employee = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Department(models.Model):
    name = models.CharField(unique=True, max_length=50)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    department_0 = models.ForeignKey(Department, models.DO_NOTHING, db_column='department_id', blank=True, null=True)  # Field renamed because of name conflict.
    job_title = models.ForeignKey('JobTitle', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'
        
class EmployeeProject(models.Model):
    pk = models.CompositePrimaryKey('employee_id', 'project_id')
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    role = models.CharField(max_length=50, blank=True, null=True)
    assigned_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_project'
        unique_together = (('employee', 'project'),)


class JobTitle(models.Model):
    title = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_title'


class Leave(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    leave_type = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave'


class ManagerRelation(models.Model):
    employee = models.OneToOneField(Employee, models.DO_NOTHING, primary_key=True)
    manager = models.ForeignKey(Employee, models.DO_NOTHING, related_name='managerrelation_manager_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager_relation'


class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    reviewer = models.ForeignKey(Employee, models.DO_NOTHING, related_name='performancereview_reviewer_set', blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performance_review'





class SalaryHistory(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary_history'