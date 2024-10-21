from django.db import models
from django.contrib.auth.models import User, Group

from AppAdmin.models import *


# Create your models here.

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_code = models.CharField(max_length=200, null=True, unique=True)  # DEPT-1
    department_name = models.TextField(max_length=100, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_department'

    def __str__(self):
        return self.department_name


# Create your models here.
class Position(models.Model):
    id = models.AutoField(primary_key=True)
    position_code = models.CharField(max_length=100, null=True, unique=True)  # POS-1
    position_name = models.TextField(max_length=100, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_position'
        ordering = ['id']

    def __str__(self):
        return self.position_name


class WorkingSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    work_sche_code = models.CharField(max_length=200, null=True, unique=True)  # SCHE-1
    work_sche_name = models.TextField(max_length=200, null=True)
    loc_code = models.ForeignKey(LocationData, to_field='loc_code', on_delete=models.CASCADE, null=True)
    over_time_ratio = models.FloatField(null=True)
    shift_start_time = models.TextField(null=True)
    shift_end_time = models.TextField(null=True)
    shift_total_hour = models.TextField(null=True)
    break_start_time = models.TextField(null=True)
    break_end_time = models.TextField(null=True)
    break_total_hour = models.TextField(null=True)
    start_time_allow = models.TextField(null=True)
    end_time_allow = models.TextField(null=True)
    total_allow_hour = models.IntegerField(null=True)
    description = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    work_day_on = models.TextField(max_length=200, null=True)
    work_day_off = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_working_schedule'

    def __str__(self):
        return self.work_sche_name

class SystemRole(models.Model):
    id = models.AutoField(primary_key=True)
    sys_role_code = models.CharField(max_length=200, null=True, unique=True)  # SYSR-1
    sys_role_name = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_system_role'

    def __str__(self):
        return self.sys_role_name


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=100, null=True, unique=True)  # EMP-1
    manager_code = models.TextField(max_length=100, null=True)
    department_code = models.ForeignKey(Department, to_field='department_code', on_delete=models.CASCADE, null=True)
    position_code = models.ForeignKey(Position, to_field='position_code', on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # work_sche_code = models.ForeignKey(WorkingSchedule, to_field='work_sche_code', on_delete=models.CASCADE, null=True)
    # sys_role_code = models.ForeignKey(SystemRole, to_field='sys_role_code', on_delete=models.CASCADE, null=True)
    status = models.TextField(max_length=200, null=True)  # Active, Block
    attendance_status = models.TextField(max_length=200, null=True)  # Pending, Approved, Rejected
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee'
        ordering = ['id']

    def __str__(self):
        return self.employee_code


class EmployeeInformation(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    first_name = models.TextField(max_length=100, null=True)
    last_name = models.TextField(max_length=100, null=True)
    title = models.TextField(max_length=100, null=True)
    title_of_courtesy = models.TextField(max_length=100, null=True)
    mobile = models.TextField(max_length=50, null=True)
    alter_mobile = models.TextField(max_length=50, null=True)
    email = models.TextField(max_length=100, null=True)
    gender = models.TextField(max_length=10, null=True)
    age = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    hire_date = models.DateField(null=True)
    duty_type = models.TextField(max_length=20, null=True)  # Full Time, Part Time, Contractual
    ethnic_group = models.TextField(max_length=20, null=True)  # Punjabi, Baloch, Sindis
    joining_date = models.DateField(null=True)
    material_status = models.TextField(max_length=20, null=True)  # Married, Divorced, Widowed, Other
    religion = models.TextField(max_length=50, null=True)
    termination_date = models.DateField(null=True)
    termination_remarks = models.TextField(max_length=200, null=True)
    address = models.TextField(max_length=200, null=True)
    area = models.TextField(max_length=100, null=True)
    city = models.TextField(max_length=200, null=True)
    state = models.TextField(max_length=200, null=True)
    country = models.TextField(max_length=200, null=True)
    emp_photo = models.ImageField(upload_to='Employee/Photo', default="")
    cnic_no = models.TextField(max_length=20, null=True)
    cnic_front = models.ImageField(upload_to='Employee/CNIC', default="")
    cnic_back = models.ImageField(upload_to='Employee/CNIC', default="")
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_information'
        ordering = ['id']

    def __str__(self):
        return self.title


class EmployeeFormat(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    first_name = models.TextField(max_length=100, null=True)
    last_name = models.TextField(max_length=100, null=True)
    title = models.TextField(max_length=100, null=True)
    mobile = models.TextField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    hire_date = models.DateField(null=True)
    address = models.TextField(max_length=200, null=True)
    city = models.TextField(max_length=200, null=True)
    state = models.TextField(max_length=200, null=True)
    cnic_no = models.TextField(max_length=20, null=True)
    status = models.TextField(max_length=200, null=True)
    remarks = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_format'
        ordering = ['id']

    def __str__(self):
        return self.title


class EmployeePaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    payment_code = models.CharField(max_length=200, null=True, unique=True)  # EPM-1
    pm_code = models.ForeignKey(PaymentMethod, to_field='pm_code', on_delete=models.CASCADE, null=True)
    bank_code = models.ForeignKey(BankData, to_field='bank_code', on_delete=models.CASCADE, null=True)
    account_title = models.TextField(max_length=100, null=True)
    account_number = models.TextField(null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_payment_method'

    def __str__(self):
        return self.payment_code


class EmployeeSalary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    salary_code = models.CharField(max_length=200, null=True, unique=True)  # SAL-1
    pay_frequency = models.TextField(max_length=100, null=True)  # Daily, Monthly
    rate_type = models.TextField(max_length=20, null=True)  # Daily, Salary, Wages
    rate_amount = models.IntegerField(null=True)
    basic_salary = models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_salary'

    def __str__(self):
        return self.employee_code


class EmployeeSalaryHistory(models.Model):
    id = models.AutoField(primary_key=True)
    salary_hist_code = models.CharField(max_length=200, null=True, unique=True)  # SALH-
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    salary_code = models.CharField(max_length=200, null=True)
    pay_frequency = models.TextField(max_length=100, null=True)
    rate_type = models.TextField(max_length=20, null=True)
    rate_amount = models.IntegerField(null=True)
    basic_salary = models.IntegerField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_salary_history'

    def __str__(self):
        return self.employee_code


class Payroll(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    payroll_code = models.CharField(max_length=200, null=True, unique=True)  # PAYR-1
    pay_date = models.DateField()
    basic_pay = models.IntegerField(null=True)
    allowances = models.IntegerField(null=True)
    deduction = models.IntegerField(null=True)
    net_pay = models.IntegerField(null=True)
    opening_bal = models.IntegerField(null=True)
    closing_bal = models.IntegerField(null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_payroll'

    def __str__(self):
        return self.employee_code


class AllowanceType(models.Model):
    id = models.AutoField(primary_key=True)
    all_type_code = models.CharField(max_length=200, null=True, unique=True)  # ATY-1
    all_type_name = models.TextField(max_length=20, null=True)  # Cash Allowance, Overtime Allowance, Internet Package
    description = models.TextField(max_length=200, null=True)
    type = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_allowance_type'

    def __str__(self):
        return self.all_type_name


class AllowanceFixed(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    all_type_code = models.ForeignKey(AllowanceType, to_field='all_type_code', on_delete=models.CASCADE, null=True)
    all_fixed_code = models.CharField(max_length=200, null=True, unique=True)  # AF-1
    allowance_amount = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_allowance_fixed'

    def __str__(self):
        return self.id


class AllowanceTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    all_type_code = models.ForeignKey(AllowanceType, to_field='all_type_code', on_delete=models.CASCADE, null=True)
    payment_code = models.ForeignKey(EmployeePaymentMethod, to_field='payment_code', on_delete=models.CASCADE,
                                     null=True)
    all_trans_code = models.CharField(max_length=200, null=True, unique=True)  # AT-1
    trans_date = models.DateField()
    trans_amount = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_allowance_trans'

    def __str__(self):
        return self.id


class DeductionType(models.Model):
    id = models.AutoField(primary_key=True)
    ded_type_code = models.CharField(max_length=200, null=True, unique=True)  # DEDTY-1
    ded_type_name = models.TextField(max_length=20, null=True)  # Advance Salary, Provident Fund, EOBI, Petrol
    type = models.TextField(max_length=200, null=True)  # Fixed or Non-Fixed
    description = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_deduction_type'

    def __str__(self):
        return self.ded_type_name


class DeductionFixed(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    ded_type_code = models.ForeignKey(DeductionType, to_field='ded_type_code', on_delete=models.CASCADE, null=True)
    ded_fixed_code = models.CharField(max_length=200, null=True, unique=True)  # DEDFIX-1
    deduction_amount = models.IntegerField(null=True)
    description = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_deduction_fixed'

    def __str__(self):
        return self.id


class DeductionTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    ded_type_code = models.ForeignKey(DeductionType, to_field='ded_type_code', on_delete=models.CASCADE, null=True)
    payment_code = models.ForeignKey(EmployeePaymentMethod, to_field='payment_code', on_delete=models.CASCADE,
                                     null=True)
    ded_trans_code = models.CharField(max_length=200, null=True, unique=True)  # DT-1
    trans_date = models.DateField()
    trans_amount = models.IntegerField(null=True)
    description = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_deduction_trans'

    def __str__(self):
        return self.id


# class WeeklyWorking(models.Model):
#     id = models.AutoField(primary_key=True)
#     work_code = models.CharField(max_length=200, null=True, unique=True)  # WORK-1
#     sche_code = models.ForeignKey(WorkingSchedule, to_field='sche_code', on_delete=models.CASCADE, null=True)
#     day_name = models.TextField(max_length=200, null=True)
#     start_time = models.DateField(max_length=200, null=True)
#     end_time = models.DateField(max_length=200, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.CharField(max_length=200, null=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     updated_by = models.CharField(max_length=200, null=True)
#
#     class Meta:
#         db_table = 'tbl_weekly_working'
#
#     def __str__(self):
#         return self.id


class EmployeeAttendance(models.Model):
    id = models.AutoField(primary_key=True)
    emp_attendance_code = models.CharField(max_length=200, null=True, unique=True)  # EA-1
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    attendance_date = models.DateField(null=True)
    check_in = models.TextField(max_length=200, null=True)
    check_out = models.TextField(max_length=200, null=True)
    net_time_spent = models.TextField(max_length=200, null=True)
    late_in = models.TextField(max_length=200, null=True)
    early_out = models.TextField(max_length=200, null=True)
    short_time = models.TextField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)  # Present, Absent
    category = models.TextField(max_length=200,
                                null=True)  # National Holiday, Emergency Holiday, Work Day, Off Day, Leave, Work From Home
    # work_from_home = models.TextField(max_length=200, null=True)  # Yes, No
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_attendance'

    def __str__(self):
        return self.emp_attendance_code


class Holiday(models.Model):
    id = models.AutoField(primary_key=True)
    holiday_code = models.CharField(max_length=200, null=True, unique=True)  # HOLI-1
    holiday_name = models.TextField(max_length=200, null=True)
    holiday_date = models.DateField(null=True)
    description = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_holiday'

    def __str__(self):
        return self.id


class LeaveType(models.Model):
    id = models.AutoField(primary_key=True)
    leave_type_code = models.CharField(max_length=200, null=True, unique=True)  # LTP-1
    leave_type_name = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_leave_type'

    def __str__(self):
        return self.leave_type_name


class LeaveSubtype(models.Model):
    id = models.AutoField(primary_key=True)
    leave_subtype_code = models.CharField(max_length=200, null=True, unique=True)  # LST-1
    leave_subtype_name = models.TextField(max_length=200, null=True)
    leave_type_code = models.ForeignKey(LeaveType, to_field='leave_type_code', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_leave_subtype'

    def __str__(self):
        return self.leave_subtype_name


class LeaveApplication(models.Model):
    id = models.AutoField(primary_key=True)
    leave_app_code = models.CharField(max_length=200, null=True, unique=True)  # LA-1
    leave_type_code = models.ForeignKey(LeaveType, to_field='leave_type_code', on_delete=models.CASCADE, null=True)
    leave_subtype_code = models.ForeignKey(LeaveSubtype, to_field='leave_subtype_code', on_delete=models.CASCADE,
                                           null=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    from_date = models.DateTimeField(null=True)
    to_date = models.DateTimeField(null=True)
    leave_category = models.TextField(max_length=200, null=True)  # Half, Full
    reason = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)  # Pending, Approved, Rejected
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_leave_application'

    def __str__(self):
        return self.id


class LeaveTaken(models.Model):
    id = models.AutoField(primary_key=True)
    leave_taken_code = models.CharField(max_length=200, null=True, unique=True)  # LTK-1
    leave_app_code = models.ForeignKey(LeaveApplication, to_field='leave_app_code', on_delete=models.CASCADE, null=True)
    reason = models.TextField(max_length=200, null=True)
    approval_by = models.TextField(max_length=200, null=True)
    approval_at = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)  # Approved, Rejected
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_leave_taken'

    def __str__(self):
        return self.id


class EmployeeLocation(models.Model):
    id = models.AutoField(primary_key=True)
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    loc_store_code = models.ForeignKey(LocationStore, to_field='loc_store_code', on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_employee_location'
        ordering = ['id']

    def __str__(self):
        return self.status


class EmergencyContact(models.Model):
    id = models.AutoField(primary_key=True)
    contact_code = models.CharField(max_length=100, null=True, unique=True)  # EC-1
    employee_code = models.ForeignKey(Employee, to_field='employee_code', on_delete=models.CASCADE, null=True)
    contact_name = models.TextField(max_length=200, null=True)
    contact_relation = models.TextField(max_length=200, null=True)
    mobile_no = models.TextField(max_length=50, null=True)
    alter_mobile_no = models.TextField(max_length=50, null=True)
    home_phone = models.TextField(max_length=50, null=True)
    alter_home_no = models.TextField(max_length=50, null=True)
    work_no = models.TextField(max_length=50, null=True)
    alter_work_no = models.TextField(max_length=50, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_emergency_contact'
        ordering = ['id']

    def __str__(self):
        return self.contact_code


class EmergencyHoliday(models.Model):
    id = models.AutoField(primary_key=True)
    emer_code = models.CharField(max_length=200, null=True, unique=True)  # HOLI-1
    emer_name = models.TextField(max_length=200, null=True)
    emer_date = models.DateField(null=True)
    description = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_emergency_holiday'

    def __str__(self):
        return self.id


class NationalHoliday(models.Model):
    id = models.AutoField(primary_key=True)
    holiday_code = models.CharField(max_length=200, null=True, unique=True)  # HOLI-1
    holiday_name = models.TextField(max_length=200, null=True)
    holiday_date = models.DateField(null=True)
    description = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_national_holiday'

    def __str__(self):
        return self.id
