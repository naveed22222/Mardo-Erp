from django.urls import re_path
from AppEmployee.views import *

urlpatterns = [
    re_path(r'^Department/', EmployeeDepartmentView, name='EmployeeDepartment'),
    re_path(r'^Position/', EmployeePositionView, name='EmployeePosition'),
    re_path(r'^Employee/Create', AddEmployeeView, name='AddEmployee'),
    re_path(r'^Employee/Upload', UploadEmployeeView, name='UploadEmployee'),
    re_path(r'^Employee/edit/(?P<code>.+)/', EditEmployeeView, name='EditEmployee'),
    re_path(r'^Employee/Search/', EmployeeDetailView, name='EmployeeDetail'),
    re_path(r'^Employee/Location/', EmployeeLocationView, name='EmployeeLocation'),
    re_path(r'^Employee/View/(?P<code>.+)/', EmployeeInformationView, name="EmployeeInformation"),
    # AJAX FUNCTION CODE
    re_path(r'add_emp_department/', AddEmployeeDepartmentView, name='AddEmployeeDepartment'),
    re_path(r'delete_emp_departmnet/', DeleteEmployeeDepartmentView, name='DeleteEmployeeDepartment'),
    re_path(r'add_emp_position/', AddEmployeePositionView, name='AddEmployeePosition'),
    re_path(r'delete_emp_position/', DeleteEmployeePositionView, name='DeleteEmployeePosition'),
    re_path(r'delete_emp_format/', DeleteEmployeeFormatVew, name='DeleteEmployeeFormat'),
    # re_path(r'get_employee_position_from_location/', GetEmployeePositionFromLocationView, name='GetEmployeePositionFromLocation'),
    re_path(r'get_employee_name_from_position_and_location/', GetEmployeeNameFromPositionAndLocationVier, name='GetEmployeeNameFromPositionAndLocation'),
    # DEDUCTION URL
    re_path(r'^Deduction/Category/', DeductionCategoryView, name='DeductionCategory'),
    re_path(r'^Deduction/Fixed/Search/', FixedDeductionDetailsView, name='FixedDeductionDetails'),
    re_path(r'^Deduction/Fixed/Create/', AddFixedDeductionView, name='AddFixedDeduction'),
    re_path(r'^Deduction/Non-Fixed/Search/', NonFixedDeductionDetailsView, name='NonFixedDeductionDetails'),
    re_path(r'^Deduction/Non-Fixed/Create/', AddNonFixedDeductionView, name='AddNonFixedDeduction'),
    # AJAX FUNCTION CODE
    re_path(r'add_deduction_category/', AddDeductionCategoryView, name='AddDeductionCategory'),
    re_path(r'delete_deduction_category/', DeleteDeductionCategoryView, name='DeleteDeductionCategory'),
    re_path(r'delete_deduction_fixed/', DeleteDeductionFixedView, name='DeleteDeductionFixed'),
    # ALLOWANCES URL
    re_path(r'^Allowance/Category/', AllowanceCategoryView, name='AllowanceCategory'),
    re_path(r'^Allowance/Fixed/Search/', FixedAllowanceDetailsView, name='FixedAllowanceDetails'),
    re_path(r'^Allowance/Fixed/Create/', AddFixedAllowanceView, name='AddFixedAllowance'),
    re_path(r'^Allowance/Non-Fixed/Search/', NonFixedAllowanceDetailsView, name='NonFixedAllowanceDetails'),
    re_path(r'^Allowance/Non-Fixed/Create/', AddNonFixedAllowanceView, name='AddNonFixedAllowance'),

    # PAYROLL
    re_path(r'^Payroll/Generate/', AddPayrollView, name='AddPayroll'),
    re_path(r'^PayrollStatement/View/', PayrollStatementView, name='PayrollStatement'),
    # AJAX FUNCTION
    re_path(r'^Payroll/payments/', MakePayerollPaymentsView, name='MakePayerollPayments'),
    # EMPLOYEE SALARY
    re_path(r'^Payroll/Salary/', UpdateMultipleEmployeeSalaryView, name='UpdateMultipleEmployeeSalary'),

    # AJAX FUNCTION CODE
    re_path(r'add_allowance_category/', AddAllowanceCategoryView, name='AddAllowanceCategory'),
    re_path(r'delete_allowance_category/', DeleteAllowanceCategoryView, name='DeleteAllowanceCategory'),
    re_path(r'delete_allowance_fixed/', DeleteFixedAllowanceView, name='DeleteFixedAllowance'),
    re_path(r'delete_allowance_nonfixed/', DeleteNonFixedAllowanceView, name='DeleteNonFixedAllowance'),
    # SINGLE EMPLOYEE ALLOWANCE  URL
    re_path(r'single_employee_fixed_allowance/', SingleEmployeeFixedAllowanceView, name='SingleEmployeeFixedAllowance'),
    re_path(r'single_employee_non_fixed_allowance/', SingleEmployeeNonFixedAllowanceView,
            name='SingleEmployeeNonFixedAllowance'),
    re_path(r'cmd_allowance_type_name/', FillCmdFixedAllowanceTypeNameView, name='FillCmdFixedAllowanceTypeName'),
    re_path(r'cmd_non_fixed_allowance_type_name/', FillCmdNonAllowanceTypeNameView, name='FillCmdNonAllowanceTypeName'),
    # SINGLE EMPLOYEE DEDUCTION URL
    re_path(r'single_employee_fixed_deduction/', SingleEmployeeFixedDeductionView, name='SingleEmployeeFixedDeduction'),
    re_path(r'cmd_deduction_type_name/', FillCmdDeductionTypeNameView, name='FillCmdDeductionTypeName'),
    re_path(r'single_employee_non_fixed_deduction/', SingleEmployeeNonFixedDeductionView,
            name='SingleEmployeeNonFixedDeduction'),
    re_path(r'cmd_non_deduction_type_name/', FillCmdNonDeductionTypeNameView, name='FillCmdNonDeductionTypeName'),
    # SINGLE EMPLOYEE SALARY FUNCTION URL
    re_path(r'update_single_employee_salary/', UpdateSingleEmployeeSalaryView, name='UpdateSingleEmployeeSalary'),
    re_path(r'salary_history_detail/', ShowSalaryHistoryDetailView, name='ShowSalaryHistoryDetail'),
    #  SINGLE EMPLOYEE LOCATION URL
    re_path(r'add_employee_location/', AddEmployeeLocationView, name='AddEmployeeLocation'),
    re_path(r'cmd_employee_location/', FillCmdEmployeeLocationView, name='FillCmdEmployeeLocation'),
    # SINGLE EMPLOYEE
    re_path(r'^PaymentMethodChangeOnEmp/', PaymentMethodChangeOnEmpView, name='PaymentMethodChangeOnEmp'),
    re_path(r'add_emp_payment/', AddEmployeePaymentView, name='AddEmployeePaymentView'),
    # LEAVE URL
    re_path(r'^National/Holiday/', NationalHolidayView, name='NationalHoliday'),
    re_path(r'^WeeklyWorking/', WeeklyWorkingView, name='WeeklyWorking'),
    re_path(r'^Leave/Type/', LeaveTypeView, name='LeaveType'),
    # AJAX FUNCTION CODE
    re_path(r'add_national_holiday/', AddNationalHolidayView, name='AddNationalHoliday'),
    re_path(r'delete_national_holiday/', DeleteNationalHolidayView, name='DeleteNationalHoliday'),
    # WEEKLY WORKING
    re_path(r'add_weekly_working/', AddWeeklyWorkingView, name='AddWeeklyWorking'),
    re_path(r'delete_Weekly_Working/', DeleteWeeklyWorkingView, name='DeleteWeeklyWorking'),
    # LEAVE TYPE
    re_path(r'add_leave_type/', AddLeaveTypeView, name='AddLeaveType'),
    re_path(r'delete_leave_type/', DeleteLeaveTypeView, name='DeleteLeaveType'),

]
