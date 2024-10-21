import json
import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connections
from AppAdmin.utils import *
from AppEmployee.forms import *
from django.db.models import Count
from datetime import datetime, timedelta
import datetime
from tablib import Dataset


# from openpyxl import load_workbook


# Create your views here.
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else str(obj)


def contains_number(string):
    return any(char.isdigit() for char in string)


# Create your views here.
@login_required(login_url='LoginView')
def EmployeeDepartmentView(request):
    message = ""
    template_name = "Employee/Department.html"

    get_search = ""
    if request.method == "POST":
        get_search = request.POST['search']
        message = "Success"

    if get_search == "":
        department_list = Department.objects.all().order_by('id')
    else:
        department_list = Department.objects.filter(department_name__iregex=get_search)

    message = message + ":" + str(get_search)

    params = {'department_list': department_list,
              'message': message}

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def AddEmployeeDepartmentView(request):
    message = ""
    get_action_type = request.POST['action_type']
    get_department_id = request.POST['department_id']
    get_department_name = request.POST['department_name']
    dateTime = datetime.datetime.now()

    if get_action_type == "NEW":

        department_auto_code = AutoGenerateCodeForModel(Department, "department_code", "DEPT-")
        key_department_code = get_department_name.strip()
        InstEmpDepartment = Department(
            department_code=department_auto_code,
            department_name=key_department_code,
            status="Active",
            created_at=dateTime,
            created_by=request.session['emp_code']
        )
        InstEmpDepartment.save()
        message = "Success"

    elif get_action_type == "UPDATE":

        key_department_code = get_department_name.strip()
        UpdateDepartment = Department.objects.get(id=get_department_id)
        UpdateDepartment.department_name = key_department_code
        UpdateDepartment.updated_at = dateTime
        UpdateDepartment.updated_by = request.session['emp_code']
        UpdateDepartment.save()
        message = "Success"

    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def AddEmployeeLocationView(request):
    message = ""
    get_action_type = request.POST['action_type']
    get_id = request.POST['location_id']
    get_employee_code = request.POST['employee_code']
    get_location_store = request.POST['cmd_location']
    get_status = request.POST['cmd_status']
    dateTime = datetime.datetime.now()

    if get_action_type == "NEW":

        InstEmpLocation = EmployeeLocation(
            employee_code_id=get_employee_code,
            loc_store_code_id=get_location_store,
            status=get_status,
            created_at=dateTime,
            created_by=request.session['emp_code']
        )
        InstEmpLocation.save()
        message = "Success"

    elif get_action_type == "UPDATE":

        UpdateLocation = EmployeeLocation.objects.get(id=get_id)
        UpdateLocation.loc_store_code_id = get_location_store
        UpdateLocation.status = get_status
        UpdateLocation.updated_at = dateTime
        UpdateLocation.updated_by = request.session['emp_code']
        UpdateLocation.save()
        message = "Success"

    # employee_location = list(EmployeeLocation.objects.filter(employee_code_id=get_employee_code).values())
    cursor = connections['default'].cursor()
    query_employee = "select  eml.id ,title as name, loc_store_name ,eml.status as status , loc_store_code_id from tbl_employee_information emi INNER JOIN tbl_employee_location eml ON emi.employee_code_id = eml.employee_code_id INNER JOIN tbl_location_store ls ON ls.loc_store_code = eml.loc_store_code_id  where eml.employee_code_id = '" + get_employee_code + "'"
    cursor.execute(query_employee)
    employee_location = DictinctFetchAll(cursor)

    param = {
        'message': message,
        'employee_location': employee_location,
    }

    return HttpResponse(json.dumps(param, default=date_handler))


@login_required(login_url='LoginView')
def UpdateSingleEmployeeSalaryView(request):
    message = ""
    get_employee_code = request.POST['employee_code']
    get_salary_code = request.POST['salary_code']
    get_pay_frequency = request.POST['get_pay_frequency']
    get_rate_type = request.POST['get_rate_type']
    get_rate_amount = request.POST['rate_amount']
    get_basic_salary = request.POST['basic_salary']
    dateTime = datetime.datetime.now()

    # SINGLE EMPLOYEE SALARY HISTORY
    employee_salary = EmployeeSalary.objects.get(employee_code_id=get_employee_code)
    salary_hist_auto_code = AutoGenerateCodeForModel(EmployeeSalaryHistory, "salary_hist_code", "SALH-")
    InstEmpSalaryHistory = EmployeeSalaryHistory(
        salary_hist_code=salary_hist_auto_code,
        employee_code_id=get_employee_code,
        salary_code=get_salary_code,
        pay_frequency=get_pay_frequency,
        rate_type=get_rate_type,
        rate_amount=get_rate_amount,
        basic_salary=get_basic_salary,
        start_date=employee_salary.start_date,
        end_date=dateTime,
        created_at=dateTime,
        created_by=request.session['emp_code']
    )
    InstEmpSalaryHistory.save()

    # UPDATE EMPLOYEE SALARY
    UpdateEmployeeSalary = EmployeeSalary.objects.get(salary_code=get_salary_code)
    UpdateEmployeeSalary.pay_frequency = get_pay_frequency
    UpdateEmployeeSalary.rate_type = get_rate_type
    UpdateEmployeeSalary.rate_amount = get_rate_amount
    UpdateEmployeeSalary.basic_salary = get_basic_salary
    UpdateEmployeeSalary.updated_at = dateTime
    UpdateEmployeeSalary.updated_by = request.session['emp_code']
    UpdateEmployeeSalary.save()
    message = "Success"

    employee_salary = list(EmployeeSalary.objects.filter(employee_code_id=get_employee_code).values())

    param = {
        'message': message,
        'employee_salary': employee_salary
    }

    return HttpResponse(json.dumps(param, default=date_handler))


@login_required(login_url='LoginView')
def ShowSalaryHistoryDetailView(request):
    get_employee_code = request.POST['employee_code']
    salary_history = list(EmployeeSalaryHistory.objects.filter(employee_code_id=get_employee_code).values())

    return HttpResponse(json.dumps({'salary_history': salary_history}, default=date_handler))


@login_required(login_url='LoginView')
def DeleteEmployeeDepartmentView(request):
    message = ""
    get_id = request.POST['id']

    delete_Department = Department.objects.get(id=get_id)
    delete_Department.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


# Create your views here.
@login_required(login_url='LoginView')
def EmployeePositionView(request):
    message = ""
    template_name = "Employee/Position.html"
    position_list = Position.objects.all().order_by('id')
    params = {'position_list': position_list}

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def AddEmployeePositionView(request):
    message = ""
    get_action_type = request.POST['action_type']
    get_position_id = request.POST['position_id']
    get_position_name = request.POST['position_name']
    dateTime = datetime.datetime.now()

    if get_action_type == "NEW":

        position_auto_code = AutoGenerateCodeForModel(Position, "position_code", "POS-")
        key_position_name = get_position_name.strip()
        InstEmpPosition = Position(
            position_code=position_auto_code,
            position_name=key_position_name,
            status="Active",
            created_at=dateTime,
            created_by=request.session['emp_code']
        )
        InstEmpPosition.save()
        message = "Success"

    elif get_action_type == "UPDATE":
        key_position_name = get_position_name.strip()
        UpdatePosition = Position.objects.get(id=get_position_id)
        UpdatePosition.position_name = key_position_name
        UpdatePosition.updated_at = dateTime
        UpdatePosition.updated_by = request.session['emp_code']
        UpdatePosition.save()
        message = "Success"

    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def DeleteEmployeePositionView(request):
    message = ""
    get_id = request.POST['id']
    delete_Position = Position.objects.get(id=get_id)
    delete_Position.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def DeleteEmployeeFormatVew(request):
    message = ""
    EmployeeFormat.objects.all().delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


# @login_required(login_url='LoginView')
# def GetEmployeePositionFromLocationView(request):
#     message = ""
#     cursor = connections['default'].cursor()
#     get_location = request.POST['store_location']
#     # CONVERT STRING INTO LIST
#     split_location = get_location.split(",")
#     # CONVERT LIST INTO TUPLE
#     if len(split_location) == 1:
#         location_tuple = tuple(split_location)
#         location = '(%s)' % ', '.join(
#             map(repr, location_tuple))
#     else:
#         # CONVERT LIST INTO TUPLE
#         location = format(tuple(split_location))
#
#     query_employee = "SELECT distinct position_code, position_name from tbl_employee_location INNER JOIN  tbl_employee on tbl_employee.employee_code = tbl_employee_location.employee_code_id INNER JOIN tbl_position on  tbl_position.position_code =  tbl_employee.position_code_id WHERE loc_store_code_id in " + location + ""
#     cursor.execute(query_employee)
#     employee_position = DictinctFetchAll(cursor)
#     message = "Success"
#     param = {
#         'message': message,
#         'cmd_list': employee_position
#     }
#     return HttpResponse(json.dumps(param))


def GetEmployeeNameFromPositionAndLocationVier(request):
    message = ""
    cursor = connections['default'].cursor()
    get_designation = request.POST['cmd_designation']
    get_location = request.POST['store_location']
    # CONVERT STRING INTO LIST
    split_location = get_location.split(",")
    # CONVERT LIST INTO TUPLE
    if len(split_location) == 1:
        location_tuple = tuple(split_location)
        location = '(%s)' % ', '.join(
            map(repr, location_tuple))
    else:
        location = format(tuple(split_location))

    query_employee = " SELECT DISTINCT employee_code, position_code_id, title FROM tbl_employee emp INNER JOIN tbl_employee_location empl on emp.employee_code = empl.employee_code_id INNER JOIN tbl_employee_information empi ON emp.employee_code = empi.employee_code_id WHERE loc_store_code_id in " + location + " and position_code_id like '" + get_designation + "'"
    cursor.execute(query_employee)
    employee_info = DictinctFetchAll(cursor)

    message = "Success"
    param = {
        'message': message,
        'cmd_list': employee_info
    }
    return HttpResponse(json.dumps(param))


@login_required(login_url='LoginView')
def FillCmdEmployeeLocationView(request):
    get_employee_code = request.POST['employee_code']
    get_cmd_location = request.POST['cmd_location']
    get_action_type = request.POST['action_type']

    cursor = connections['default'].cursor()
    store_location = LocationStore.objects.all()
    query_employee_location = "select loc_store_name, loc_store_code, employee_code_id from tbl_location_store lcs inner JOIN tbl_employee_location empl ON lcs.loc_store_code = empl.loc_store_code_id where employee_code_id = '" + get_employee_code + "'"
    cursor.execute(query_employee_location)
    employee_location = DictinctFetchAll(cursor)
    emp_store_location = []

    if get_action_type == "NEW":
        for i in range(len(store_location)):
            employee_location_dict = dict()
            loc_store_code = store_location[i].loc_store_code
            loc_store_name = store_location[i].loc_store_name
            employee_location_dict["loc_store_code"] = loc_store_code
            employee_location_dict["loc_store_name"] = loc_store_name
            emp_store_location.append(employee_location_dict)
            for j in range(len(employee_location)):
                emp_store_code = employee_location[j]['loc_store_code']
                if loc_store_code == emp_store_code:
                    emp_store_location.pop()

    if get_action_type == "UPDATE":
        for i in range(len(store_location)):
            employee_location_dict = dict()
            loc_store_code = store_location[i].loc_store_code
            loc_store_name = store_location[i].loc_store_name
            employee_location_dict["loc_store_code"] = loc_store_code
            employee_location_dict["loc_store_name"] = loc_store_name
            emp_store_location.append(employee_location_dict)
            for j in range(len(employee_location)):
                emp_store_code = employee_location[j]['loc_store_code']
                if loc_store_code == emp_store_code:
                    emp_store_location.pop()
        employee_location_dict = dict()
        employee_location = LocationStore.objects.get(loc_store_code=get_cmd_location)
        employee_location_dict["loc_store_code"] = employee_location.loc_store_code
        employee_location_dict["loc_store_name"] = employee_location.loc_store_name
        emp_store_location.append(employee_location_dict)

    return HttpResponse(json.dumps({'cmd_list': emp_store_location}, default=date_handler))


@login_required(login_url='LoginView')
def SingleEmployeeFixedDeductionView(request):
    get_action_type = request.POST['action_type']
    get_employee_code = request.POST['employee_code']
    get_ded_fix_code = request.POST['ded_type_code']
    get_ded_type_name = request.POST['ded_type_name']
    get_ded_amount = request.POST['ded_amount']

    if get_action_type == 'NEW':
        fixed_ded_auto_code = AutoGenerateCodeForModel(DeductionFixed, "ded_fixed_code", "DEDFIX-")
        FixedDeduction = DeductionFixed(
            ded_fixed_code=fixed_ded_auto_code,
            employee_code_id=get_employee_code,
            ded_type_code_id=get_ded_type_name,
            deduction_amount=get_ded_amount,
            created_by=request.session['username']
        )
        FixedDeduction.save()
    elif get_action_type == 'UPDATE':
        FixedDeduction = DeductionFixed.objects.get(ded_fixed_code=get_ded_fix_code)
        FixedDeduction.ded_type_code_id = get_ded_type_name
        FixedDeduction.deduction_amount = get_ded_amount
        FixedDeduction.updated_at = datetime.datetime.now()
        FixedDeduction.updated_by = request.session['username']
        FixedDeduction.save()

    cursor = connections['default'].cursor()
    query_deduction = "SELECT ded_fixed_code,ded_type_code, ded_type_name, deduction_amount FROM tbl_employee_deduction_fixed df INNER JOIN tbl_employee_deduction_type dt ON df.ded_type_code_id = dt.ded_type_code where employee_code_id= '" + get_employee_code + "'"
    cursor.execute(query_deduction)
    fixed_deduction = DictinctFetchAll(cursor)
    param = {
        'fixed_deduction': fixed_deduction
    }
    return HttpResponse(json.dumps(param, default=date_handler))


@login_required(login_url='LoginView')
def SingleEmployeeNonFixedDeductionView(request):
    get_action_type = request.POST['action_type']
    get_employee_code = request.POST['employee_code']
    get_ded_trans_code = request.POST['ded_type_code']
    get_ded_type_name = request.POST['ded_type_name']
    get_payment_method = request.POST['payment_method']
    get_ded_date = request.POST['ded_date']
    get_ded_amount = request.POST['ded_amount']

    if get_action_type == 'NEW':
        trans_ded_auto_code = AutoGenerateCodeForModel(DeductionTransaction, "ded_trans_code", "DT-")
        TransDeduction = DeductionTransaction(
            ded_trans_code=trans_ded_auto_code,
            employee_code_id=get_employee_code,
            ded_type_code_id=get_ded_type_name,
            payment_code_id=get_payment_method,
            trans_date=get_ded_date,
            trans_amount=get_ded_amount,
            created_by=request.session['username']
        )
        TransDeduction.save()
    elif get_action_type == 'UPDATE':
        TransDeduction = DeductionTransaction.objects.get(ded_trans_code=get_ded_trans_code)
        TransDeduction.ded_type_code_id = get_ded_type_name
        TransDeduction.payment_code_id = get_payment_method
        TransDeduction.trans_date = get_ded_date
        TransDeduction.trans_amount = get_ded_amount
        TransDeduction.updated_at = datetime.datetime.now()
        TransDeduction.updated_by = request.session['username']
        TransDeduction.save()

    cursor = connections['default'].cursor()
    # query_deduction = "SELECT ded_trans_code,ded_type_code, ded_type_name, trans_date , trans_amount , payment_code, account_title FROM tbl_employee_deduction_trans df INNER JOIN tbl_employee_deduction_type dt ON df.ded_type_code_id = dt.ded_type_code INNER JOIN tbl_employee_payment_method epm ON df.payment_code_id = epm.payment_code where df.employee_code_id= '" + get_employee_code + "'"
    # cursor.execute(query_deduction)
    # trans_deduction = DictinctFetchAll(cursor)

    query_employee_trans_ded = "with sub as (select ded_trans_code ,payment_code_id, edt.employee_code_id, trans_amount, trans_date, ded_type_code_id, ded_type_name , account_title ,account_number, pm_code_id,bank_code_id from tbl_employee_deduction_trans edt LEFT OUTER JOIN tbl_employee_deduction_type AS dt ON edt.ded_type_code_id = dt.ded_type_code LEFT OUTER JOIN tbl_employee_payment_method epm ON epm.payment_code = edt.payment_code_id WHERE edt.employee_code_id = '" + get_employee_code + "') select ded_trans_code, payment_code_id, employee_code_id, trans_amount, trans_date, ded_type_code_id, ded_type_name , account_title ,account_number, pm_code_id, bank_code_id ,pm_name , bank_name from sub LEFT OUTER JOIN tbl_payment_method pm ON sub.pm_code_id = pm.pm_code LEFT OUTER JOIN tbl_bank_data bank ON sub.bank_code_id = bank.bank_code"
    cursor.execute(query_employee_trans_ded)
    trans_deduction = DictinctFetchAll(cursor)
    param = {
        'trans_deduction': trans_deduction
    }
    return HttpResponse(json.dumps(param, default=date_handler))


@login_required(login_url='LoginView')
def SingleEmployeeFixedAllowanceView(request):
    get_action_type = request.POST['action_type']
    get_employee_code = request.POST['employee_code']
    get_all_fix_code = request.POST['all_type_code']
    get_all_type_name = request.POST['all_type_name']
    get_all_amount = request.POST['all_amount']

    if get_action_type == 'NEW':
        fixed_all_auto_code = AutoGenerateCodeForModel(AllowanceFixed, "all_fixed_code", "AF-")
        FixedAllowance = AllowanceFixed(
            all_fixed_code=fixed_all_auto_code,
            employee_code_id=get_employee_code,
            all_type_code_id=get_all_type_name,
            allowance_amount=get_all_amount,
            created_by=request.session['username']
        )
        FixedAllowance.save()
    elif get_action_type == 'UPDATE':
        FixedAllowance = AllowanceFixed.objects.get(all_fixed_code=get_all_fix_code)
        FixedAllowance.all_type_code_id = get_all_type_name
        FixedAllowance.allowance_amount = get_all_amount
        FixedAllowance.updated_at = datetime.datetime.now()
        FixedAllowance.updated_by = request.session['username']
        FixedAllowance.save()

    cursor = connections['default'].cursor()
    query_allowance = "SELECT all_fixed_code,all_type_code, all_type_name, allowance_amount FROM tbl_employee_allowance_fixed df INNER JOIN tbl_employee_allowance_type dt ON df.all_type_code_id = dt.all_type_code where employee_code_id= '" + get_employee_code + "'"
    cursor.execute(query_allowance)
    fixed_allowance = DictinctFetchAll(cursor)
    param = {
        'fixed_allowance': fixed_allowance
    }
    return HttpResponse(json.dumps(param, default=date_handler))


@login_required(login_url='LoginView')
def SingleEmployeeNonFixedAllowanceView(request):
    get_action_type = request.POST['action_type']
    get_employee_code = request.POST['employee_code']
    get_all_trans_code = request.POST['all_type_code']
    get_all_type_name = request.POST['all_type_name']
    get_payment_method = request.POST['payment_method']
    get_all_date = request.POST['all_date']
    get_all_amount = request.POST['all_amount']

    if get_action_type == 'NEW':
        trans_all_auto_code = AutoGenerateCodeForModel(AllowanceTransaction, "all_trans_code", "AT-")
        TransAllowance = AllowanceTransaction(
            all_trans_code=trans_all_auto_code,
            employee_code_id=get_employee_code,
            all_type_code_id=get_all_type_name,
            payment_code_id=get_payment_method,
            trans_date=get_all_date,
            trans_amount=get_all_amount,
            created_by=request.session['username']
        )
        TransAllowance.save()
    elif get_action_type == 'UPDATE':
        TransAllowance = AllowanceTransaction.objects.get(all_trans_code=get_all_trans_code)
        TransAllowance.all_type_code_id = get_all_type_name
        TransAllowance.payment_code_id = get_payment_method
        TransAllowance.trans_date = get_all_date
        TransAllowance.trans_amount = get_all_amount
        TransAllowance.updated_at = datetime.datetime.now()
        TransAllowance.updated_by = request.session['username']
        TransAllowance.save()

    cursor = connections['default'].cursor()
    query_employee_trans_all = "with sub as (select all_trans_code, trans_date, trans_amount, all_type_code_id, elt.employee_code_id, payment_code_id ,all_type_name , account_title ,account_number, pm_code_id,bank_code_id from tbl_employee_allowance_trans elt LEFT OUTER JOIN tbl_employee_allowance_type lt ON elt.all_type_code_id = lt.all_type_code LEFT OUTER JOIN tbl_employee_payment_method epm ON epm.payment_code = elt.payment_code_id WHERE elt.employee_code_id = '" + get_employee_code + "') select all_trans_code, trans_date, trans_amount, all_type_code_id, employee_code_id, payment_code_id ,all_type_name , account_title ,account_number, pm_code_id,bank_code_id,pm_name , bank_name from sub LEFT OUTER JOIN tbl_payment_method pm ON sub.pm_code_id = pm.pm_code LEFT OUTER JOIN tbl_bank_data bank ON sub.bank_code_id = bank.bank_code"
    cursor.execute(query_employee_trans_all)
    trans_allowance = DictinctFetchAll(cursor)

    param = {
        'trans_allowance': trans_allowance
    }
    return HttpResponse(json.dumps(param, default=date_handler))


@login_required(login_url='LoginView')
def AddEmployeeView(request):
    message = ""
    template_name = "Employee/AddEmployee.html"
    dateTime = datetime.datetime.now()

    format_str = '%Y-%m-%d'
    today_date = dateTime.strftime(format_str)

    form = FormEmployeeInfo()
    if request.method == "POST":
        form_class = FormEmployeeInfo(request.POST)

        if form_class.is_valid():
            get_form_inst = form_class.save(commit=False)

            get_department_name = request.POST['cmd_department']
            get_position = request.POST['cmd_position']
            get_manager = request.POST['cmd_manager']

            get_country = request.POST['cmd_country']
            get_state = request.POST['cmd_state']
            get_city = request.POST['cmd_city']
            get_area = request.POST['cmd_area']

            # INSERT INTO EMPLOYEE MODEL
            auto_employee_code = AutoGenerateCodeForModel(Employee, 'employee_code', 'EMP-')
            InstEmployee = Employee(
                employee_code=auto_employee_code,
                department_code_id=get_department_name,
                position_code_id=get_position,
                manager_code=get_manager,
                work_sche_code_id="SCHE-1",
                # sys_role_code_id="SYSR-5",
                status="Active",
                created_at=dateTime,
                created_by=request.session['emp_code']
            )
            InstEmployee.save()
            # INSERT INTO EMPLOYEE MODEL (END)

            # INSERT EMPLOYEE INFORMATION IN MODEL (START)
            get_birth_date = request.POST['birth_date']
            birth_date_part = get_birth_date.split("-")
            retrive_age = calculateAge(date(int(birth_date_part[0]), int(birth_date_part[1]), int(birth_date_part[2])))

            get_hire_date = request.POST['hire_date']
            # format_str = '%Y-%m-%d'
            # str_today_date = datetime.datetime.now().strftime(format_str)
            # today_date =datetime.datetime.strptime(str_today_date, format_str).date()
            # hire_date_format =datetime.datetime.strptime(get_hire_date, format_str).date()
            # if today_date > hire_date_format:
            #     pass
            # else:
            #     pass

            get_mobile_no = request.POST['phone']

            getFirstName = get_form_inst.first_name
            getLastName = get_form_inst.last_name
            setTitleName = getFirstName + " " + getLastName

            get_form_inst.employee_code_id = auto_employee_code
            get_form_inst.birth_date = get_birth_date
            get_form_inst.age = retrive_age
            get_form_inst.hire_date = get_hire_date
            get_form_inst.mobile = get_mobile_no
            get_form_inst.title = setTitleName
            get_form_inst.country = get_country
            get_form_inst.state = get_state
            get_form_inst.city = get_city
            get_form_inst.area = get_area
            get_form_inst.created_at = dateTime
            get_form_inst.created_by = request.session['emp_code']
            get_form_inst.save()
            # INSERT EMPLOYEE INFORMATION IN MODEL (START)

            # INSERT EMPLOYEE SALARY DATA IN MODEL (START)
            get_pay_freguency = request.POST['cmd_pay_freguency']
            get_rate_type = request.POST['cmd_rate_type']
            get_rate_amount = request.POST['rate_amount']
            get_basic_salary = request.POST['basic_salary']

            get_store_location = request.POST.getlist('store_location')

            # Store Location Information
            get_len_store_location = len(get_store_location)
            if get_len_store_location > 0:

                for i in range(get_len_store_location):
                    InstLocation = EmployeeLocation(
                        employee_code_id=auto_employee_code,
                        loc_store_code_id=get_store_location[i],
                        status='Active',
                        created_at=dateTime,
                        created_by=request.session['emp_code']
                    )
                    InstLocation.save()

            set_emp_salary_code = AutoGenerateCodeForModel(EmployeeSalary, 'salary_code', 'SAL-')
            InstSalary = EmployeeSalary(
                employee_code_id=auto_employee_code,
                salary_code=set_emp_salary_code,
                pay_frequency=get_pay_freguency,
                rate_type=get_rate_type,
                rate_amount=get_rate_amount,
                basic_salary=get_basic_salary,
                start_date=dateTime,
                created_at=dateTime,
                created_by=request.session['emp_code']
            )
            InstSalary.save()
            # INSERT EMPLOYEE SALARY DATA IN MODEL (END)

            # INSERT EMPLOYEE PAYMENT METHOD DATA IN MODEL (START)
            get_cmd_payment = request.POST['cmd_payment']
            auto_payment_code = AutoGenerateCodeForModel(EmployeePaymentMethod, 'payment_code', 'EPM-')
            InstEmpPaymentMethod = EmployeePaymentMethod(
                employee_code_id=auto_employee_code,
                payment_code=auto_payment_code,
                pm_code_id=get_cmd_payment,
                account_title="Cash",
                status="Active",
                created_at=dateTime,
                created_by=request.session['emp_code']
            )
            InstEmpPaymentMethod.save()
            # INSERT EMPLOYEE EMERGENCY CONTACT
            get_emergency_contact_name = request.POST['contact_name']
            get_emergency_contact_relation = request.POST['contact_relation']
            get_emergency_mobile_no = request.POST['emergency_mobile_no']
            get_emergency_alter_mobile_no = request.POST['emergency_alter_mobile_no']
            get_home_phone = request.POST['home_phone']
            get_alter_home_phone = request.POST['alter_home_phone']
            get_work_number = request.POST['work_number']
            get_alter_work_number = request.POST['alter_work_number']

            auto_emergency_contact_code = AutoGenerateCodeForModel(EmergencyContact, 'contact_code', 'EC-')
            InstEmpEmergencyContact = EmergencyContact(
                employee_code_id=auto_employee_code,
                contact_code=auto_emergency_contact_code,
                contact_name=get_emergency_contact_name,
                contact_relation=get_emergency_contact_relation,
                mobile_no=get_emergency_mobile_no,
                alter_mobile_no=get_emergency_alter_mobile_no,
                home_phone=get_home_phone,
                alter_home_no=get_alter_home_phone,
                work_no=get_work_number,
                alter_work_no=get_alter_work_number,
                created_at=dateTime,
                created_by=request.session['emp_code']
            )
            InstEmpEmergencyContact.save()

            # GENERATE NEW EMPLOYEE ATTENDANCE (START)
            # GET SINGLE EMPLOYEE LIST
            get_single_emp_detail = list(EmployeeInformation.objects.filter(employee_code_id=auto_employee_code))

            # GET ALL EMPLOYEE LIST
            Emp_list = list(Employee.objects.filter(employee_code=auto_employee_code))

            if len(get_single_emp_detail) > 0:

                # GET MONTH START DATE (START)
                d_part = today_date.split("-")
                month_start_date = datetime.date(int(d_part[0]), int(d_part[1]), int(1))
                # GET MONTH START DATE (END)

                # GET TOTAL MISSING ATTENDANCE DAYS OF CURRENT MONTH (START)
                no_of_days = days_between(str(month_start_date), today_date)
                # GET TOTAL MISSING ATTENDANCE DAYS OF CURRENT MONTH  (END)

                # GET YESTERDAY DATE
                yesterday = (datetime.datetime.now() - timedelta(days=1)).strftime(format_str)
                date_count = 1

                # GET PREVIOUS DAYS COUNT AND DATE (START)
                for j in range(no_of_days):

                    # YESTERDAY DATE ATTENDANCE
                    emp_atten_details = list(EmployeeAttendance.objects.filter(attendance_date=yesterday,
                                                                               employee_code=auto_employee_code))

                    if len(emp_atten_details) == 0:
                        date_count += 1

                        # GET PREVIOUS DATES (START)
                        yesterday_format = str(yesterday) + " 00:00:00"
                        yesterday_date_format = datetime.datetime.strptime(yesterday_format,
                                                                           '%Y-%m-%d %H:%M:%S').date()
                        yesterday = (yesterday_date_format - timedelta(days=1)).strftime(format_str)
                        # GET PREVIOUS DATES (END)

                    # IF LENGTH IS GREATER THAN ZERO THEN BREAK THE LOOP
                    elif len(emp_atten_details) > 0:
                        break
                # GET PREVIOUS DAYS COUNT AND DATE (END)

                save_date = yesterday

                # SAVE EMPLOYEE REMAINING DAYS ATTENDANCE (START)
                for k in range(date_count):
                    # GET NEXT DATES (START)
                    save_format = str(save_date) + " 05:00:00"
                    save_date_format = datetime.datetime.strptime(save_format, '%Y-%m-%d %H:%M:%S').date()
                    get_day_format = save_date_format + timedelta(days=1)
                    save_date = get_day_format.strftime(format_str)
                    # GET NEXT DATES (START)

                    InstanceCheckEmpAttendanceStatus(save_date, Emp_list)
                # SAVE EMPLOYEE REMAINING DAYS ATTENDANCE (END)
            # GENERATE NEW EMPLOYEE ATTENDANCE (END)

            message = "Success"
    else:
        message = "Error"

    department_list = Department.objects.all().order_by('department_name')
    position_list = Position.objects.all().order_by('position_name')
    payment_list = PaymentMethod.objects.filter(pm_name="Cash")
    location_store_list = LocationStore.objects.all()

    params = {'form': form,
              'department_list': department_list,
              'position_list': position_list,
              'payment_list': payment_list,
              'location_store_list': location_store_list,
              'message': message,
              }

    return render(request, template_name, params)


def InstanceCheckEmpAttendanceStatus(get_date, Emp_list):
    # GET DAY NAME (START)
    save_format = str(get_date) + " 05:00:00"
    save_date_format = datetime.datetime.strptime(save_format, '%Y-%m-%d %H:%M:%S').date()
    get_day = save_date_format.strftime("%A")
    # GET DAY NAME (END)

    category = ""
    status = ""

    # CHECK NATIONAL HOLIDAY
    national_holiday_detail = list(NationalHoliday.objects.filter(holiday_date=get_date))
    if len(national_holiday_detail) > 0:
        category = "National Holiday"
    else:
        # CHECK EMERGENCY HOLIDAY
        emergency_holiday_detail = list(EmergencyHoliday.objects.filter(emer_date=get_date))
        if len(emergency_holiday_detail) > 0:
            category = "Emergency Holiday"

    # GET EMPLOYEE LIST
    for i in range(len(Emp_list)):
        get_emp_code = Emp_list[i].employee_code
        get_work_sche = Emp_list[i].work_sche_code_id

        # GET WORK SCHEDULE OF EMPLOYEE
        work_sche_list = list(WorkingSchedule.objects.filter(work_sche_code=get_work_sche))

        if len(work_sche_list) > 0:

            if category == "National Holiday" or category == "Emergency Holiday":
                pass
            else:
                # GET WORKING SCHEDULE AND CHECK WORK DAY IS ON OR OFF (START)
                work_status = "Yes"
                work_sche_detail = work_sche_list[0]
                save_working_days_off = work_sche_detail.work_day_off
                save_working_days_off_array = save_working_days_off.split(',')

                # CHECK WORKING DAY
                for m in range(len(save_working_days_off_array)):
                    if save_working_days_off_array[m].strip(" ") == get_day:
                        work_status = "No"

                if work_status == "No":
                    category = "Off Day"
                else:
                    # CHECK EMPLOYEE LEAVE (START)
                    leave_app_detail = list(
                        LeaveApplication.objects.filter(employee_code_id=get_emp_code, status="Approved",
                                                        from_date__gte=get_date, to_date__lte=get_date))

                    if len(leave_app_detail) > 0:
                        category = "Leave"
                    else:
                        category = "Work Day"
                        status = "Absent"
                    # CHECK EMPLOYEE LEAVE (END)
                # GET WORKING SCHEDULE AND CHECK WORK DAY IS ON OR OFF (END)

            # SAVE EMPLOYEE ATTENDANCE (START)
            attendance_auto_generate = AutoGenerateCodeForModel(EmployeeAttendance,
                                                                "emp_attendance_code",
                                                                "EA-")

            # GENERATE EMPLOYEE ATTENDANCE (START)
            InstEmpAttendance = EmployeeAttendance(
                emp_attendance_code=attendance_auto_generate,
                employee_code_id=get_emp_code,
                status=status,
                category=category,
                attendance_date=get_date,
                created_at=datetime,
                created_by="Auto",
            )
            InstEmpAttendance.save()
            # GENERATE EMPLOYEE ATTENDANCE (END)

            message = "Success"
            # SAVE EMPLOYEE ATTENDANCE (END)

    return


@login_required(login_url='LoginView')
def UploadEmployeeView(request):
    template_name = "Employee/UploadEmployee.html"
    remarks = ""
    message = ""
    dateTime = datetime.datetime.now()

    format_str = '%Y-%m-%d'
    today_date = dateTime.strftime(format_str)

    if request.method == 'POST':
        action_type = request.POST['action_value']

        if action_type == 'upload':
            dataset = Dataset()
            new_Excel_Sheet_Data = request.FILES['excel_file']
            get_sheet = new_Excel_Sheet_Data.name
            format = get_sheet.split(".")[1]
            imported_data = dataset.load(new_Excel_Sheet_Data.read(), format)

            for data in imported_data:
                get_full_name = data[0],
                get_mobile_no = str(data[1]),
                get_cnic = str(data[2]),
                get_birth_date = data[3],
                get_hire_date = data[4],
                get_address = data[5],
                get_city = data[6],
                get_state = data[7],

                # CHECK IF THE MOBILE AND CNIC HAS ANY STRING (LETTER) THEN CONSIDERED AS 0
                cnic_no = any(c.isalpha() for c in get_cnic[0])
                if cnic_no == True:
                    get_cnic = 0
                else:
                    get_cnic = get_cnic[0]

                mobile_no = any(c.isalpha() for c in get_mobile_no[0])
                if mobile_no == True:
                    get_mobile_no = 0
                else:
                    get_mobile_no = get_mobile_no[0]

                # SPLIT NAME INTO TWO VARIABLES
                if get_full_name[0] != None:
                    first_name, *last = get_full_name[0].split()
                    last_name = " ".join(last)

                    # ASSIGN DEFAULT BIRTH DATE AND HIRE DATE IF DATE FORMAT IS INVALID
                    birth_date_string = str(get_birth_date[0])
                    hire_date_string = str(get_hire_date[0])
                    format = "%Y-%m-%d %H:%M:%S"
                    # FOR BIRTH DATE
                    try:
                        datetime.datetime.strptime(birth_date_string, format)
                        message = "Success"
                    except ValueError:
                        message = "Error"

                    if message == "Error":
                        birth_date_string = '2000-01-01 00:00:00'
                    # FOR HIRE DATE
                    try:
                        datetime.datetime.strptime(hire_date_string, format)
                        message = "Success"
                    except ValueError:
                        message = "Error"

                    if message == "Error":
                        hire_date_string = '2000-01-01 00:00:00'

                    format_hire_date = datetime.datetime.strptime(hire_date_string, '%Y-%m-%d %H:%M:%S').date()
                    # GET AGE THROUGH BIRTH DATE
                    format_birth_date = datetime.datetime.strptime(birth_date_string, '%Y-%m-%d %H:%M:%S').date()
                    birth_date_part = str(format_birth_date).split("-")
                    retrive_age = calculateAge(
                        date(int(birth_date_part[0]), int(birth_date_part[1]), int(birth_date_part[2])))
                    # SAVE EXCEL RECORD IN TABLE
                    InstEmployeeFormat = EmployeeFormat(
                        first_name=first_name,
                        last_name=last_name,
                        title=get_full_name[0],
                        mobile=get_mobile_no,
                        age=retrive_age,
                        birth_date=format_birth_date,
                        hire_date=format_hire_date,
                        address=get_address[0],
                        city=get_city[0],
                        state=get_state[0],
                        cnic_no=get_cnic,
                        status="Pending",
                        created_at=dateTime,
                        created_by=request.session['emp_code']
                    )
                    InstEmployeeFormat.save()
                    message = "Success"

        if action_type == 'save':
            get_row_length = int(request.POST['row_length'])
            get_department = request.POST['str_department']
            get_position = request.POST['str_position']
            get_duty_type = request.POST['str_duty_type']
            get_title = request.POST['str_title']
            get_mobile = request.POST['str_mobile']
            get_cnic = request.POST['str_cnic']
            get_birth_date = request.POST['str_birth_date']
            get_gender = request.POST['str_gender']
            get_hire_date = request.POST['str_hire_date']
            get_location = request.POST['str_location']
            get_pay_frequency = request.POST['str_pay_frequency']
            get_rate_type = request.POST['str_rate_type']
            get_rate_amount = request.POST['str_rate_amount']
            get_basic_salary = request.POST['str_basic_salary']
            get_address = request.POST['str_address']
            get_city = request.POST['str_city']
            get_state = request.POST['str_state']
            # SPLIT CODE
            split_department_code = get_department.split("^")
            split_position_code = get_position.split("^")
            split_duty_type = get_duty_type.split("^")
            split_title = get_title.split("^")
            split_mobile = get_mobile.split("^")
            split_cnic = get_cnic.split("^")
            split_birth_date = get_birth_date.split("^")
            split_gender = get_gender.split("^")
            split_hire_date = get_hire_date.split("^")
            split_location = get_location.split("^")
            split_pay_frequency = get_pay_frequency.split("^")
            split_rate_type = get_rate_type.split("^")
            split_rate_amount = get_rate_amount.split("^")
            split_basic_salary = get_basic_salary.split("^")
            split_address = get_address.split("^")
            split_city = get_city.split("^")
            split_state = get_state.split("^")

            if get_row_length > 0:
                for i in range(get_row_length):
                    remarks = ""
                    department_code = split_department_code[i]
                    position_code = split_position_code[i]
                    duty_type = split_duty_type[i]
                    title = split_title[i]
                    mobile = split_mobile[i]
                    cnic = split_cnic[i]
                    birth_date = split_birth_date[i]
                    gender = split_gender[i]
                    hire_date = split_hire_date[i]
                    location = split_location[i]
                    pay_frequency = split_pay_frequency[i]
                    rate_type = split_rate_type[i]
                    rate_amount = split_rate_amount[i]
                    basic_salary = split_basic_salary[i]
                    address = split_address[i]
                    city = split_city[i]
                    state = split_state[i]

                    if department_code == "NA":
                        remarks += "department_code,"

                    if position_code == "NA":
                        remarks += "position_code,"

                    if title == "NA":
                        remarks += "name,"

                    if mobile == "NA":
                        remarks += "mobile,"

                    if birth_date == "NA":
                        remarks += "birth_date,"

                    if hire_date == "NA":
                        remarks += "hire_date,"

                    if location == '':
                        remarks += "location,"

                    if pay_frequency == "NA":
                        remarks += "pay_frequency,"

                    if rate_type == "NA":
                        remarks += "rate_type,"

                    if len(remarks) == 0:
                        # SPLIT NAME INTO TWO VARIABLES
                        first_name, *last = title.split()
                        last_name = " ".join(last)

                        format_birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d').date()
                        format_hire_date = datetime.datetime.strptime(hire_date, '%Y-%m-%d').date()

                        # INSERT INTO EMPLOYEE MODEL
                        auto_employee_code = AutoGenerateCodeForModel(Employee, 'employee_code', 'EMP-')
                        InstEmployee = Employee(
                            employee_code=auto_employee_code,
                            department_code_id=department_code,
                            position_code_id=position_code,
                            status="Active",
                            created_at=dateTime,
                            created_by=request.session['emp_code']
                        )
                        InstEmployee.save()

                        # EMPLOYEE INFORMATION
                        InstEmployeeInformation = EmployeeInformation(
                            employee_code_id=auto_employee_code,
                            first_name=first_name,
                            last_name=last_name,
                            title=title,
                            mobile=mobile,
                            gender=gender,
                            birth_date=format_birth_date,
                            hire_date=format_hire_date,
                            duty_type=duty_type,
                            cnic_no=cnic,
                            city=city,
                            state=state,
                            address=address,
                            created_at=dateTime,
                            created_by=request.session['emp_code']
                        )
                        InstEmployeeInformation.save()

                        # Store Location Information
                        get_location = location.split(',')
                        get_len_store_location = len(get_location)
                        if get_len_store_location > 0:

                            for i in range(get_len_store_location):
                                InstLocation = EmployeeLocation(
                                    employee_code_id=auto_employee_code,
                                    loc_store_code_id=get_location[i],
                                    status='Active',
                                    created_at=dateTime,
                                    created_by=request.session['emp_code']
                                )
                                InstLocation.save()

                        # EMPLOYEE SALARY
                        set_emp_salary_code = AutoGenerateCodeForModel(EmployeeSalary, 'salary_code', 'SAL-')
                        InstSalary = EmployeeSalary(
                            employee_code_id=auto_employee_code,
                            salary_code=set_emp_salary_code,
                            pay_frequency=pay_frequency,
                            rate_type=rate_type,
                            rate_amount=rate_amount,
                            basic_salary=basic_salary,
                            start_date=dateTime,
                            created_at=dateTime,
                            created_by=request.session['emp_code']
                        )
                        InstSalary.save()

                        # EMPLOYEE PAYMENT METHOD
                        auto_payment_code = AutoGenerateCodeForModel(EmployeePaymentMethod, 'payment_code', 'EPM-')
                        InstEmpPaymentMethod = EmployeePaymentMethod(
                            employee_code_id=auto_employee_code,
                            payment_code=auto_payment_code,
                            pm_code_id='PM-1',
                            account_title="Cash",
                            status="Active",
                            created_at=dateTime,
                            created_by=request.session['emp_code']
                        )
                        InstEmpPaymentMethod.save()

                        # GENERATE NEW EMPLOYEE ATTENDANCE (START)
                        # GET SINGLE EMPLOYEE LIST
                        get_single_emp_detail = list(
                            EmployeeInformation.objects.filter(employee_code_id=auto_employee_code))

                        # GET ALL EMPLOYEE LIST
                        Emp_list = list(Employee.objects.filter(employee_code=auto_employee_code))

                        if len(get_single_emp_detail) > 0:

                            # GET MONTH START DATE (START)
                            d_part = today_date.split("-")
                            month_start_date = datetime.date(int(d_part[0]), int(d_part[1]), int(1))
                            # GET MONTH START DATE (END)

                            # GET TOTAL MISSING ATTENDANCE DAYS OF CURRENT MONTH (START)
                            no_of_days = days_between(str(month_start_date), today_date)
                            # GET TOTAL MISSING ATTENDANCE DAYS OF CURRENT MONTH  (END)

                            # GET YESTERDAY DATE
                            yesterday = (datetime.datetime.now() - timedelta(days=1)).strftime(format_str)
                            date_count = 1

                            # GET PREVIOUS DAYS COUNT AND DATE (START)
                            for j in range(no_of_days):

                                # YESTERDAY DATE ATTENDANCE
                                emp_atten_details = list(EmployeeAttendance.objects.filter(attendance_date=yesterday,
                                                                                           employee_code=auto_employee_code))

                                if len(emp_atten_details) == 0:
                                    date_count += 1

                                    # GET PREVIOUS DATES (START)
                                    yesterday_format = str(yesterday) + " 00:00:00"
                                    yesterday_date_format = datetime.datetime.strptime(yesterday_format,
                                                                                       '%Y-%m-%d %H:%M:%S').date()
                                    yesterday = (yesterday_date_format - timedelta(days=1)).strftime(format_str)
                                    # GET PREVIOUS DATES (END)

                                # IF LENGTH IS GREATER THAN ZERO THEN BREAK THE LOOP
                                elif len(emp_atten_details) > 0:
                                    break
                            # GET PREVIOUS DAYS COUNT AND DATE (END)

                            save_date = yesterday

                            # SAVE EMPLOYEE REMAINING DAYS ATTENDANCE (START)
                            for k in range(date_count):
                                # GET NEXT DATES (START)
                                save_format = str(save_date) + " 05:00:00"
                                save_date_format = datetime.datetime.strptime(save_format, '%Y-%m-%d %H:%M:%S').date()
                                get_day_format = save_date_format + timedelta(days=1)
                                save_date = get_day_format.strftime(format_str)
                                # GET NEXT DATES (START)

                                InstanceCheckEmpAttendanceStatus(save_date, Emp_list)
                            # SAVE EMPLOYEE REMAINING DAYS ATTENDANCE (END)
                        # GENERATE NEW EMPLOYEE ATTENDANCE (END)

                            FormatEmployee = EmployeeFormat.objects.get(title=title)
                            FormatEmployee.employee_code_id = auto_employee_code
                            FormatEmployee.status = "Approved"
                            FormatEmployee.remarks = remarks
                            FormatEmployee.updated_at = dateTime
                            FormatEmployee.updated_by = request.session['emp_code']
                            FormatEmployee.save()
                            message = "Success"
                        else:
                            FormatEmployee = EmployeeFormat.objects.get(title=title)
                            FormatEmployee.remarks = remarks
                            FormatEmployee.save()
                            message = "Success"

        if action_type == 'delete':
            EmployeeFormat.objects.filter(status='Pending').delete()

    department_list = Department.objects.all().order_by('department_name')
    position_list = Position.objects.all().order_by('position_name')
    location_store_list = LocationStore.objects.all()
    employee_format = EmployeeFormat.objects.filter(status='Pending')

    params = {
        'department_list': department_list,
        'position_list': position_list,
        'location_store_list': location_store_list,
        'employee_format': employee_format,
        'message': message,
    }

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def EditEmployeeView(request, code):
    employee_code = code
    message = ""
    template_name = "Employee/EditEmployee.html"
    dateTime = datetime.datetime.now()
    form = FormEmployeeInfo()
    if request.method == "POST":
        employee_inst = EmployeeInformation.objects.get(employee_code_id=employee_code)
        employee_inst_form = FormEmployeeInfo(request.POST, request.FILES, instance=employee_inst)
        employee_form = employee_inst_form.save(commit=False)
        employee_form.save()
        # UPDATE EMPLOYEE DEPARTMENT AND POSITION
        get_department_name = request.POST['cmd_department']
        get_position = request.POST['cmd_position']
        get_manager = request.POST['cmd_manager']

        get_country = request.POST['cmd_country']
        get_state = request.POST['cmd_state']
        get_city = request.POST['cmd_city']
        get_area = request.POST['cmd_area']

        if get_manager == 'NA':
            get_manager = None
        employee = Employee.objects.get(employee_code=employee_code)
        employee.department_code_id = get_department_name
        employee.position_code_id = get_position
        employee.manager_code = get_manager
        employee.save()

        # UPDATE EMPLOYEE INFORMATION
        get_birth_date = request.POST['birth_date']
        birth_date_part = get_birth_date.split("-")
        retrive_age = calculateAge(date(int(birth_date_part[0]), int(birth_date_part[1]), int(birth_date_part[2])))

        get_hire_date = request.POST['hire_date']
        get_mobile_no = request.POST['phone']

        getFirstName = employee_inst.first_name
        getLastName = employee_inst.last_name
        setTitleName = getFirstName + " " + getLastName

        employee_information = EmployeeInformation.objects.get(employee_code_id=employee_code)
        employee_information.birth_date = get_birth_date
        employee_information.age = retrive_age
        employee_information.hire_date = get_hire_date
        employee_information.mobile = get_mobile_no
        employee_information.title = setTitleName
        employee_information.country = get_country
        employee_information.state = get_state
        employee_information.city = get_city
        employee_information.area = get_area
        employee_information.update_at = dateTime
        employee_information.updated_by = setTitleName
        employee_information.save()

        # UPDATE EMPLOYEE SALARY
        get_pay_freguency = request.POST['cmd_pay_freguency']
        get_rate_type = request.POST['cmd_rate_type']
        get_rate_amount = request.POST['rate_amount']
        get_basic_salary = request.POST['basic_salary']
        employee_salary = EmployeeSalary.objects.get(employee_code_id=employee_code)
        employee_salary.pay_frequency = get_pay_freguency
        employee_salary.rate_type = get_rate_type
        employee_salary.rate_amount = get_rate_amount
        employee_salary.basic_salary = get_basic_salary
        employee_salary.save()

        # UPDATE EMPLOYEE LOCATION
        get_store_location = request.POST.getlist('store_location')
        # DELETE EMPLOYEE PREVIOUS LOCATION AND ADD NEW LOCATIONS
        employee_location = EmployeeLocation.objects.filter(employee_code_id=employee_code)
        if len(employee_location) > 0:
            for i in range(len(employee_location)):
                employee_location[i].delete()

        get_len_store_location = len(get_store_location)
        if get_len_store_location > 0:
            for i in range(get_len_store_location):
                InstLocation = EmployeeLocation(
                    employee_code_id=employee_code,
                    loc_store_code_id=get_store_location[i],
                    status='Active',
                    created_at=dateTime,
                    created_by=request.session['emp_code']
                )
                InstLocation.save()
                message = 'Success'
    else:
        form = FormEmployeeInfo()
    employee = Employee.objects.get(employee_code=employee_code)
    employee_supervision_info = Employee.objects.filter(employee_code=employee.manager_code)
    if len(employee_supervision_info) > 0:
        employee_supervision_info = employee_supervision_info[0]
    employee_information = EmployeeInformation.objects.get(employee_code_id=employee_code)
    employee_salary = EmployeeSalary.objects.get(employee_code_id=employee_code)
    employee_location = EmployeeLocation.objects.filter(employee_code_id=employee_code)
    employee_emergency_contact = EmergencyContact.objects.get(employee_code_id=employee_code)
    # GET EMPLOYEE STORE LOCATION CODE IN ARRAY
    employee_location_array = []

    if len(employee_location) > 0:
        for i in range(len(employee_location)):
            employee_location_array.append(employee_location[i].loc_store_code_id)

    department_list = Department.objects.all().order_by('department_name')
    position_list = Position.objects.all().order_by('position_name')
    payment_list = PaymentMethod.objects.filter(pm_name="Cash")
    location_store_list = LocationStore.objects.all()

    params = {
        'form': form,
        'message': message,
        'department_list': department_list,
        'position_list': position_list,
        'payment_list': payment_list,
        'employee_information': employee_information,
        'employee_salary': employee_salary,
        'employee_location': employee_location,
        'location_store_list': location_store_list,
        'employee_location_array': employee_location_array,
        'employee_supervision_info': employee_supervision_info,
        'employee_emergency_contact': employee_emergency_contact,
        'employee': employee,
    }

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def EmployeeLocationView(request):
    template_name = "Employee/EmployeeLocation.html"
    # employee_location = EmployeeLocation.objects.all()
    cursor = connections['default'].cursor()
    query_employee = "select  eml.id ,  title as name, loc_store_name ,eml.status as status from tbl_employee_information emi INNER JOIN tbl_employee_location eml ON emi.employee_code_id = eml.employee_code_id INNER JOIN tbl_location_store ls ON ls.loc_store_code = eml.loc_store_code_id"
    cursor.execute(query_employee)
    employee_location = DictinctFetchAll(cursor)

    param = {
        'employee_location': employee_location
    }
    return render(request, template_name, param)


@login_required(login_url='LoginView')
def EmployeeDetailView(request):
    message = ""
    template_name = "Employee/EmployeeDetail.html"

    cursor = connections['default'].cursor()
    query_employee = "WITH emp AS(SELECT employee_code, department_code_id, position_code_id, manager_code, status FROM tbl_employee ORDER BY id) SELECT employee_code, manager_code, empi.title AS title, empinf.title AS manager_name, empi.emp_photo, empi.mobile, empi.hire_date, emp.status, department_name, position_name, pay_frequency, rate_type, rate_amount, basic_salary FROM emp LEFT OUTER JOIN tbl_employee_department dept ON emp.department_code_id = dept.department_code LEFT OUTER JOIN tbl_position AS pos ON emp.position_code_id = pos.position_code LEFT OUTER JOIN tbl_employee_information AS empi ON emp.employee_code = empi.employee_code_id LEFT OUTER JOIN tbl_employee_information AS empinf ON emp.manager_code = empinf.employee_code_id LEFT OUTER JOIN tbl_employee_salary AS emps ON emp.employee_code = emps.employee_code_id ORDER BY SPLIT_PART(emp.employee_code, '-', 2)::INTEGER;"
    cursor.execute(query_employee)
    employee_list = DictinctFetchAll(cursor)

    query_employee_location = "select employee_code_id, loc_store_code, loc_store_name from tbl_employee_location empl INNER JOIN tbl_location_store ls ON empl.loc_store_code_id=ls.loc_store_code"
    cursor.execute(query_employee_location)
    employee_location = DictinctFetchAll(cursor)

    employee_location_list = []

    for i in range(len(employee_list)):
        employee_code = employee_list[i]['employee_code']

        location_list = []
        for j in range(len(employee_location)):
            employee_code_location = employee_location[j]['employee_code_id']
            if employee_code == employee_code_location:
                loc_store_code = employee_location[j]['loc_store_code']
                loc_store_name = employee_location[j]['loc_store_name']
                get_city_code = LocationStore.objects.get(loc_store_code=loc_store_code).city_code_id
                location_city = LocationCity.objects.get(city_code=get_city_code).city_name
                location_name = location_city + "-" + loc_store_name

                location_list.append(location_name)
                # location_list.append(employee_location[j]['loc_store_name'])

        employee_location_dict = dict()

        if len(location_list) == 0:
            employee_location_dict["employee_location"] = ''
        elif len(location_list) > 0:
            employee_location_dict["employee_location"] = '^^'.join(location_list)

        employee_location_dict["hire_date"] = employee_list[i]['hire_date']
        employee_location_dict["employee_code"] = employee_list[i]['employee_code']
        employee_location_dict["name"] = employee_list[i]['title']
        employee_location_dict["mobile"] = employee_list[i]['mobile']
        employee_location_dict["department_name"] = employee_list[i]['department_name']
        employee_location_dict["position_name"] = employee_list[i]['position_name']
        employee_location_dict["manager_name"] = employee_list[i]['manager_name']
        employee_location_dict["pay_frequency"] = employee_list[i]['pay_frequency']
        employee_location_dict["rate_type"] = employee_list[i]['rate_type']
        employee_location_dict["basic_salary"] = employee_list[i]['basic_salary']
        employee_location_dict["status"] = employee_list[i]['status']
        employee_location_list.append(employee_location_dict)

    params = {
        'employee_location_list': employee_location_list
    }

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def EmployeeInformationView(request, code):
    get_employee_code = code
    template_name = "Employee/EmployeeView.html"

    cursor = connections['default'].cursor()

    # SINGLE ORDER DETAILS
    employee_List = list(Employee.objects.filter(employee_code=get_employee_code))[0]
    employee_info = list(EmployeeInformation.objects.filter(employee_code_id=get_employee_code))[0]
    salary_info = EmployeeSalary.objects.filter(employee_code_id=get_employee_code)
    employee_salary = salary_info[0]

    payment_info = EmployeePaymentMethod.objects.filter(employee_code_id=get_employee_code)
    attendance_info = EmployeeAttendance.objects.filter(employee_code_id=get_employee_code)
    employee_fix_deduction = DeductionFixed.objects.filter(employee_code_id=get_employee_code)
    employee_fix_allowance = AllowanceFixed.objects.filter(employee_code_id=get_employee_code)
    employee_emergency_contact = EmergencyContact.objects.filter(employee_code_id=get_employee_code)[0]

    # FOR EMPLOYEE LOCATION
    query_employee = "select  eml.id ,title as name, loc_store_name ,eml.status as status , loc_store_code_id from tbl_employee_information emi INNER JOIN tbl_employee_location eml ON emi.employee_code_id = eml.employee_code_id INNER JOIN tbl_location_store ls ON ls.loc_store_code = eml.loc_store_code_id  where eml.employee_code_id = '" + get_employee_code + "'"
    cursor.execute(query_employee)
    employee_location = DictinctFetchAll(cursor)

    # FOR DEDUCTION TRANSACTION AND ITS PAYMENT METHOD
    query_employee_trans_ded = "with sub as (select ded_trans_code ,payment_code_id, edt.employee_code_id, trans_amount, trans_date, ded_type_code_id, ded_type_name , account_title ,account_number, pm_code_id,bank_code_id from tbl_employee_deduction_trans edt LEFT OUTER JOIN tbl_employee_deduction_type AS dt ON edt.ded_type_code_id = dt.ded_type_code LEFT OUTER JOIN tbl_employee_payment_method epm ON epm.payment_code = edt.payment_code_id WHERE edt.employee_code_id = '" + get_employee_code + "') select ded_trans_code, payment_code_id, employee_code_id, trans_amount, trans_date, ded_type_code_id, ded_type_name , account_title ,account_number, pm_code_id, bank_code_id ,pm_name , bank_name from sub LEFT OUTER JOIN tbl_payment_method pm ON sub.pm_code_id = pm.pm_code LEFT OUTER JOIN tbl_bank_data bank ON sub.bank_code_id = bank.bank_code"
    cursor.execute(query_employee_trans_ded)
    employee_trans_deduction = DictinctFetchAll(cursor)

    # FOR ALLOWANCE TRANSACTION AND ITS PAYMENT METHOD
    query_employee_trans_all = "with sub as (select all_trans_code, trans_date, trans_amount, all_type_code_id, elt.employee_code_id, payment_code_id ,all_type_name , account_title ,account_number, pm_code_id,bank_code_id from tbl_employee_allowance_trans elt LEFT OUTER JOIN tbl_employee_allowance_type lt ON elt.all_type_code_id = lt.all_type_code LEFT OUTER JOIN tbl_employee_payment_method epm ON epm.payment_code = elt.payment_code_id WHERE elt.employee_code_id = '" + get_employee_code + "') select all_trans_code, trans_date, trans_amount, all_type_code_id, employee_code_id, payment_code_id ,all_type_name , account_title ,account_number, pm_code_id,bank_code_id,pm_name , bank_name from sub LEFT OUTER JOIN tbl_payment_method pm ON sub.pm_code_id = pm.pm_code LEFT OUTER JOIN tbl_bank_data bank ON sub.bank_code_id = bank.bank_code"
    cursor.execute(query_employee_trans_all)
    employee_trans_allowance = DictinctFetchAll(cursor)

    # THIS QUERY IS USED IN PROFILE INFO FOR DISPLAY SINGLE EMPLOYEE LOCATIONS
    query_single_employee_location = "with res As(select loc_store_code, loc_store_name, city_code_id,loc_code_id, city_name, loc_name  from tbl_location_store ls INNER JOIN  tbl_location_city lc ON ls.city_code_id = lc.city_code INNER JOIN tbl_location_data ld ON ls.loc_code_id = ld.loc_code) select loc_store_code, loc_store_name, city_code_id,loc_code_id, city_name, loc_name, employee_code_id, empl.status from res INNER JOIN tbl_employee_location empl on empl.loc_store_code_id=res.loc_store_code where employee_code_id = '" + get_employee_code + "' and status = 'Active'"
    cursor.execute(query_single_employee_location)
    single_employee_location = DictinctFetchAll(cursor)

    params = {'employee_List': employee_List,
              'employee_info': employee_info,
              'salary_info': salary_info,
              'employee_salary': employee_salary,
              'get_employee_code': get_employee_code,
              'payment_info': payment_info,
              'attendance_info': attendance_info,
              'employee_location': employee_location,
              'employee_fix_deduction': employee_fix_deduction,
              'employee_trans_deduction': employee_trans_deduction,
              'employee_fix_allowance': employee_fix_allowance,
              'employee_trans_allowance': employee_trans_allowance,
              'single_employee_location': single_employee_location,
              'employee_emergency_contact': employee_emergency_contact,

              }

    return render(request, template_name, params)


def AddEmployeePaymentView(request):
    message = ""
    get_action_type = request.POST['action_type']
    get_payment_method = request.POST['cmd_payment_method_id']
    get_employee_payment_id = request.POST['employee_payment_id']
    get_bank_name = request.POST['cmd_bank_name_id']
    get_account_title = request.POST['account_title']
    get_account_number = request.POST['account_number']
    get_hidden_emp_code = request.POST['hidden_emp_code']
    dateTime = datetime.datetime.now()

    split_pm_code_and_name = get_payment_method.split("^^")
    pm_code = split_pm_code_and_name[0]
    pm_name = split_pm_code_and_name[1].lower()

    if pm_name != "bank":
        get_bank_name = None

    if get_action_type == "NEW":
        payment_auto_code = AutoGenerateCodeForModel(EmployeePaymentMethod, "payment_code", "EPM-")
        InstEmpPayment = EmployeePaymentMethod(
            payment_code=payment_auto_code,
            pm_code_id=pm_code,
            bank_code_id=get_bank_name,
            account_title=get_account_title,
            account_number=get_account_number,
            employee_code_id=get_hidden_emp_code,
            status="Active",
            created_at=dateTime,
            created_by=request.session['username'],
        )
        InstEmpPayment.save()
        message = "Success"

    elif get_action_type == "UPDATE":
        UpdatePayment = EmployeePaymentMethod.objects.get(id=get_employee_payment_id)
        UpdatePayment.pm_code_id = pm_code
        UpdatePayment.bank_code_id = get_bank_name
        UpdatePayment.account_title = get_account_title
        UpdatePayment.account_number = get_account_number
        UpdatePayment.updated_at = dateTime
        UpdatePayment.updated_by = request.session['username']
        UpdatePayment.save()
        message = "Success"

    cursor = connections['default'].cursor()
    query_employee_att = "SELECT emp_pm.id, payment_code, COALESCE(bank_code_id, '-') AS bank_code_id, COALESCE(account_title, '-') AS account_title, COALESCE(account_number, '-') AS account_number, emp_pm.status, pm_code_id, pm_name FROM tbl_employee_payment_method AS emp_pm LEFT OUTER JOIN tbl_payment_method AS pm ON emp_pm.pm_code_id = pm.pm_code WHERE employee_code_id = '" + get_hidden_emp_code + "';"
    cursor.execute(query_employee_att)
    payment_list = DictinctFetchAll(cursor)

    param = {
        'message': message,
        'payment_list': payment_list
    }
    return HttpResponse(json.dumps(param))


# Add Employee Payment Method Without Refresh Used for both Fixed and NonFixed
# @login_required(login_url='LoginView')
# def AddEmpPayMethodWithoutRefreshView(request):
#     message = ""
#     get_emp_code = request.POST['hidden_emp_code']
#     cursor = connections['default'].cursor()
#     query_employee_att = "SELECT emp_pm.id, payment_code, bank_code_id, account_title, account_number, emp_pm.status, pm_code_id, pm_name FROM tbl_employee_payment_method AS emp_pm LEFT OUTER JOIN tbl_payment_method AS pm ON emp_pm.pm_code_id = pm.pm_code WHERE employee_code_id = '" + get_emp_code + "'"
#     cursor.execute(query_employee_att)
#     payment_list = DictinctFetchAll(cursor)
#
#     params = {
#         'payment_list': payment_list,
#         'message': message
#     }
#
#     return HttpResponse(json.dumps(params, default=date_handler))


# EMPLOYEE START

# DEDUCTION START
def DeductionCategoryView(request):
    message = ""
    template_name = "Deduction/DeductionCategory.html"
    category_list = DeductionType.objects.all().order_by('id')
    params = {'category_list': category_list}

    return render(request, template_name, params)


def AddDeductionCategoryView(request):
    message = ""
    get_action_type = request.POST['action_type']
    get_ded_type_code = request.POST['ded_type_code']
    get_ded_type = request.POST['ded_type']
    get_ded_type_name = request.POST['ded_type_name']
    dateTime = datetime.datetime.now()

    if get_action_type == "NEW":
        deduction_type_auto_code = AutoGenerateCodeForModel(DeductionType, "ded_type_code", "DEDTY-")
        key_deduction_type = get_ded_type_name.strip()

        InstEmpCategory = DeductionType(
            ded_type_code=deduction_type_auto_code,
            type=get_ded_type,
            ded_type_name=key_deduction_type,
            status="Active",
            created_at=dateTime,
            created_by=request.session['username'],
        )
        InstEmpCategory.save()
        message = "Success"

    elif get_action_type == "UPDATE":
        key_deduction_type = get_ded_type_name.strip()
        UpdateDeduction = DeductionType.objects.get(id=get_ded_type_code)
        UpdateDeduction.ded_type_name = key_deduction_type
        UpdateDeduction.type = get_ded_type
        UpdateDeduction.updated_at = dateTime
        UpdateDeduction.updated_by = request.session['username']
        UpdateDeduction.save()
        message = "Success"

    return HttpResponse(json.dumps({'message': message}))


def DeleteDeductionCategoryView(request):
    message = ""
    get_id = request.POST['id']
    delete_category = DeductionType.objects.get(id=get_id)
    delete_category.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def FixedDeductionDetailsView(request):
    message = ""
    template_name = "Deduction/Fixed/FixedDeduction.html"
    cursor = connections['default'].cursor()
    query_fixed_deduction = "select ded_fixed_code, title, deduction_amount,df.description, ded_type_name from tbl_employee_deduction_fixed df INNER JOIN tbl_employee_deduction_type dt ON df.ded_type_code_id = dt.ded_type_code INNER JOIN tbl_employee_information emp ON df.employee_code_id = emp.employee_code_id"
    cursor.execute(query_fixed_deduction)
    deduction_list = DictinctFetchAll(cursor)

    params = {'deduction_list': deduction_list}

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def AddFixedDeductionView(request):
    message = ""
    template_name = "Deduction/Fixed/AddFixedDeduction.html"
    dateTime = datetime.datetime.now()
    if request.method == "POST":
        get_row_length = int(request.POST['row_length'])
        get_employee_code = request.POST['str_employee_code']
        get_ded_type = request.POST['str_ded_type']
        get_ded_amount = request.POST['str_ded_amount']
        # SPLIT CODE
        split_employee_code = get_employee_code.split("^")
        split_ded_type = get_ded_type.split("^")
        split_ded_amount = get_ded_amount.split("^")

        if get_row_length > 0:

            for i in range(get_row_length):
                employee_code = split_employee_code[i]
                ded_type = split_ded_type[i]
                ded_amount = split_ded_amount[i]
                # INSERT FIXED DEDUCTION
                deduction_fixed_auto_code = AutoGenerateCodeForModel(DeductionFixed, "ded_fixed_code", "DEDFIX-")
                FixedDeduction = DeductionFixed()
                FixedDeduction.employee_code_id = employee_code
                FixedDeduction.ded_type_code_id = ded_type
                FixedDeduction.ded_fixed_code = deduction_fixed_auto_code
                FixedDeduction.deduction_amount = ded_amount
                FixedDeduction.created_at = dateTime
                FixedDeduction.created_by = request.session['username']
                FixedDeduction.save()
                message = "Success"

    employee_list = EmployeeInformation.objects.all().order_by('id')
    params = {
        'message': message,
        'employee_list': employee_list,
    }
    return render(request, template_name, params)


@login_required(login_url='LoginView')
def DeleteDeductionFixedView(request):
    message = ""
    get_id = request.POST['id']
    delete_deduction_fixed = DeductionFixed.objects.get(id=get_id)
    delete_deduction_fixed.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def NonFixedDeductionDetailsView(request):
    template_name = "Deduction/Non-Fixed/NonFixedDeduction.html"
    cursor = connections['default'].cursor()
    query_employee_ded_trans = "with sub as (select ded_trans_code ,payment_code_id, edt.employee_code_id, trans_amount, trans_date, ded_type_code_id, ded_type_name , account_title ,account_number, pm_code_id,bank_code_id from tbl_employee_deduction_trans edt LEFT OUTER JOIN tbl_employee_deduction_type AS dt ON edt.ded_type_code_id = dt.ded_type_code LEFT OUTER JOIN tbl_employee_payment_method epm ON epm.payment_code = edt.payment_code_id ) select ded_trans_code, payment_code_id, sub.employee_code_id, trans_amount, trans_date, ded_type_code_id, ded_type_name , account_title ,account_number, pm_code_id, bank_code_id ,pm_name , bank_name , title from sub LEFT OUTER JOIN tbl_payment_method pm ON sub.pm_code_id = pm.pm_code LEFT OUTER JOIN tbl_bank_data bank ON sub.bank_code_id = bank.bank_code LEFT OUTER JOIN tbl_employee_information empi ON sub.employee_code_id = empi.employee_code_id"
    cursor.execute(query_employee_ded_trans)
    deduction_trans_list = DictinctFetchAll(cursor)
    params = {'deduction_trans_list': deduction_trans_list}

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def AddNonFixedDeductionView(request):
    message = ""
    template_name = "Deduction/Non-Fixed/AddNonFixedDeduction.html"
    dateTime = datetime.datetime.now()
    if request.method == "POST":
        get_row_length = int(request.POST['row_length'])
        get_employee_code = request.POST['str_employee_code']
        get_payment_method = request.POST['str_payment_method']
        get_ded_type = request.POST['str_ded_type']
        get_ded_amount = request.POST['str_ded_amount']
        get_ded_date = request.POST['str_ded_date']
        # SPLIT CODE
        split_employee_code = get_employee_code.split("^")
        split_payment_method = get_payment_method.split("^")
        split_ded_type = get_ded_type.split("^")
        split_ded_amount = get_ded_amount.split("^")
        split_ded_date = get_ded_date.split("^")

        if get_row_length > 0:

            for i in range(get_row_length):
                employee_code = split_employee_code[i]
                payment_method = split_payment_method[i]
                ded_type = split_ded_type[i]
                ded_amount = split_ded_amount[i]
                ded_date = split_ded_date[i]
                # INSERT TRANSACTION DEDUCTION
                deduction_trans_auto_code = AutoGenerateCodeForModel(DeductionTransaction, "ded_trans_code", "DT-")
                TransDeduction = DeductionTransaction()
                TransDeduction.employee_code_id = employee_code
                TransDeduction.ded_type_code_id = ded_type
                TransDeduction.payment_code_id = payment_method
                TransDeduction.ded_trans_code = deduction_trans_auto_code
                TransDeduction.trans_amount = ded_amount
                TransDeduction.trans_date = ded_date
                TransDeduction.created_at = dateTime
                TransDeduction.created_by = request.session['username']
                TransDeduction.save()
                message = "Success"

    employee_list = EmployeeInformation.objects.all().order_by('id')
    params = {'employee_list': employee_list,
              'message': message}

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def PaymentMethodChangeOnEmpView(request):
    message = ""

    emp_code = request.POST['cmd_employee']
    cursor = connections['default'].cursor()
    query_employee_pm = "WITH epms AS(SELECT employee_code_id, payment_code AS emp_pm_code, pm_code_id, pm_name, bank_code_id, account_title, account_number FROM tbl_employee_payment_method AS epm INNER JOIN tbl_payment_method AS pm ON epm.pm_code_id = pm.pm_code WHERE employee_code_id = '" + emp_code + "' ORDER BY epm.id) SELECT employee_code_id, emp_pm_code, pm_code_id, pm_name, bank_code_id, bank_name, account_title, account_number FROM epms LEFT OUTER JOIN tbl_bank_data AS bank ON epms.bank_code_id = bank.bank_code; "
    cursor.execute(query_employee_pm)
    emp_pay_method_list = DictinctFetchAll(cursor)

    params = {
        'emp_pay_method_list': emp_pay_method_list,
        'message': message
    }

    return HttpResponse(json.dumps(params, default=date_handler))


# DEDUCTION END
# ALLOWANCE START
@login_required(login_url='LoginView')
def AllowanceCategoryView(request):
    message = ""
    template_name = "Allowance/AllowanceCategory.html"
    Allowance_list = AllowanceType.objects.all().order_by('id')
    params = {'Allowance_list': Allowance_list}

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def AddAllowanceCategoryView(request):
    message = ""
    get_action_type = request.POST['action_type']
    get_all_type_id = request.POST['all_type_id']
    get_all_type = request.POST['all_type']
    get_all_type_name = request.POST['all_type_name']
    dateTime = datetime.datetime.now()

    if get_action_type == "NEW":
        all_type_auto_code = AutoGenerateCodeForModel(AllowanceType, "all_type_code", "ATY-")
        key_all_type_name = get_all_type_name.strip()
        InstEmpCategory = AllowanceType(
            all_type_code=all_type_auto_code,
            type=get_all_type,
            all_type_name=key_all_type_name,
            status="Active",
            created_at=dateTime,
            created_by=request.session['username'],
        )
        InstEmpCategory.save()
        message = "Success"

    elif get_action_type == "UPDATE":
        key_all_type_name = get_all_type_name.strip()
        UpdateAllowanceType = AllowanceType.objects.get(id=get_all_type_id)
        UpdateAllowanceType.type = get_all_type
        UpdateAllowanceType.all_type_name = key_all_type_name
        UpdateAllowanceType.updated_at = dateTime
        UpdateAllowanceType.updated_by = request.session['username']
        UpdateAllowanceType.save()
        message = "Success"

    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def DeleteAllowanceCategoryView(request):
    message = ""
    get_id = request.POST['id']
    delete_category = AllowanceType.objects.get(id=get_id)
    delete_category.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def FixedAllowanceDetailsView(request):
    template_name = "Allowance/Fixed/FixedAllowance.html"

    cursor = connections['default'].cursor()
    query_fixed_allowance = "SELECT all_fixed_code, allowance_amount, fal.description, title, all_type_name FROM tbl_employee_allowance_fixed fal INNER JOIN tbl_employee_allowance_type alt On fal.all_type_code_id = alt.all_type_code INNER JOIN tbl_employee_information emp ON fal.employee_code_id = emp.employee_code_id"
    cursor.execute(query_fixed_allowance)
    allowance_list = DictinctFetchAll(cursor)
    params = {'allowance_list': allowance_list}

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def DeleteFixedAllowanceView(request):
    message = ""
    get_id = request.POST['id']
    delete_allowance_fixed = AllowanceFixed.objects.get(id=get_id)
    delete_allowance_fixed.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def AddFixedAllowanceView(request):
    message = ""
    template_name = "Allowance/Fixed/AddFixedAllowance.html"
    dateTime = datetime.datetime.now()
    if request.method == "POST":
        get_row_length = int(request.POST['row_length'])
        get_employee_code = request.POST['str_employee_code']
        get_all_type = request.POST['str_all_type']
        get_all_amount = request.POST['str_all_amount']
        # SPLIT CODE
        split_employee_code = get_employee_code.split("^")
        split_all_type = get_all_type.split("^")
        split_all_amount = get_all_amount.split("^")

        if get_row_length > 0:

            for i in range(get_row_length):
                employee_code = split_employee_code[i]
                all_type = split_all_type[i]
                all_amount = split_all_amount[i]
                # INSERT FIXED ALLOWANCE
                allowance_fixed_auto_code = AutoGenerateCodeForModel(AllowanceFixed, "all_fixed_code", "AF-")
                FixedAllowance = AllowanceFixed()
                FixedAllowance.employee_code_id = employee_code
                FixedAllowance.all_type_code_id = all_type
                FixedAllowance.all_fixed_code = allowance_fixed_auto_code
                FixedAllowance.allowance_amount = all_amount
                FixedAllowance.created_at = dateTime
                FixedAllowance.created_by = request.session['username']
                FixedAllowance.save()
                message = "Success"

    employee_list = EmployeeInformation.objects.all().order_by('id')

    params = {
        'message': message,
        'employee_list': employee_list,
    }

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def DeleteAllowanceFixedView(request):
    message = ""
    get_id = request.POST['id']
    delete_allowance_fixed = AllowanceFixed.objects.get(id=get_id)
    delete_allowance_fixed.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def NonFixedAllowanceDetailsView(request):
    message = ""
    template_name = "Allowance/Non-Fixed/NonFixedAllowance.html"
    # allowance_list = AllowanceTransaction.objects.all().order_by('id')

    cursor = connections['default'].cursor()
    query_non_fixed_allowance = "with sub as (select all_trans_code, trans_date, trans_amount, all_type_code_id, elt.employee_code_id, payment_code_id ,all_type_name , account_title ,account_number, pm_code_id,bank_code_id from tbl_employee_allowance_trans elt LEFT OUTER JOIN tbl_employee_allowance_type lt ON elt.all_type_code_id = lt.all_type_code LEFT OUTER JOIN tbl_employee_payment_method epm ON epm.payment_code = elt.payment_code_id ) select all_trans_code, trans_date, trans_amount, all_type_code_id, sub.employee_code_id, payment_code_id ,all_type_name , account_title ,account_number, pm_code_id,bank_code_id,pm_name , bank_name, title from sub LEFT OUTER JOIN tbl_payment_method pm ON sub.pm_code_id = pm.pm_code LEFT OUTER JOIN tbl_bank_data bank ON sub.bank_code_id = bank.bank_code LEFT OUTER JOIN tbl_employee_information empi ON sub.employee_code_id = empi.employee_code_id"
    cursor.execute(query_non_fixed_allowance)
    allowance_list = DictinctFetchAll(cursor)
    params = {'allowance_list': allowance_list}

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def AddNonFixedAllowanceView(request):
    message = ""
    template_name = "Allowance/Non-Fixed/AddNonFixedAllowance.html"
    dateTime = datetime.datetime.now()

    if request.method == "POST":
        get_row_length = int(request.POST['row_length'])
        get_employee_code = request.POST['str_employee_code']
        get_payment_method = request.POST['str_payment_method']
        get_all_type = request.POST['str_all_type']
        get_all_amount = request.POST['str_all_amount']
        get_all_date = request.POST['str_all_date']
        # SPLIT CODE
        split_employee_code = get_employee_code.split("^")
        split_payment_method = get_payment_method.split("^")
        split_all_type = get_all_type.split("^")
        split_all_amount = get_all_amount.split("^")
        split_all_date = get_all_date.split("^")

        if get_row_length > 0:

            for i in range(get_row_length):
                employee_code = split_employee_code[i]
                payment_method = split_payment_method[i]
                ded_type = split_all_type[i]
                ded_amount = split_all_amount[i]
                ded_date = split_all_date[i]
                # INSERT Allowance DEDUCTION
                allowance_trans_auto_code = AutoGenerateCodeForModel(AllowanceTransaction, "all_trans_code", "AT-")
                TransAllowance = AllowanceTransaction()
                TransAllowance.employee_code_id = employee_code
                TransAllowance.all_type_code_id = ded_type
                TransAllowance.payment_code_id = payment_method
                TransAllowance.all_trans_code = allowance_trans_auto_code
                TransAllowance.trans_amount = ded_amount
                TransAllowance.trans_date = ded_date
                TransAllowance.created_at = dateTime
                TransAllowance.created_by = request.session['username']
                TransAllowance.save()
                message = "Success"

    employee_list = EmployeeInformation.objects.all().order_by('id')
    params = {
        'message': message,
        'employee_list': employee_list,

    }

    return render(request, template_name, params)


@login_required(login_url='LoginView')
def DeleteNonFixedAllowanceView(request):
    message = ""
    get_id = request.POST['id']
    delete_allowance_non_fixed = AllowanceTransaction.objects.get(id=get_id)
    delete_allowance_non_fixed.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


# ALLOWANCE END
# PAYROLL VIEW (START)
@login_required(login_url='LoginView')
def AddPayrollView(request):
    message = ""
    template_name = "Payroll/GenerateSalary.html"

    format_str = '%Y-%m-%d'
    date = datetime.datetime.now().strftime(format_str)
    cursor = connections['default'].cursor()

    # GET CURRENT MONTH AND YEAR
    d_part = date.split("-")
    current_date = datetime.date(int(d_part[0]), int(d_part[1]), int(d_part[2]))
    current_year = int(d_part[0])
    month = int(d_part[1])
    current_month = '{0:02}'.format(month)
    current_month_year = str(current_year) + "-" + str(current_month)
    if request.method == "POST":
        action_value = request.POST['action']
        if action_value == "not_generated":
            message = ""
        if action_value == "generated":
            # GET PREVIOUS MONTH AND YEAR
            start_current_date = current_date.replace(day=1)
            prev_end_date_from_current_date = start_current_date - timedelta(days=1)
            prev_month_from_current_date = prev_end_date_from_current_date.month
            prev_month_2digit = '{0:02}'.format(prev_month_from_current_date)
            prev_year_from_current_date = prev_end_date_from_current_date.year
            previous_month_year = str(prev_year_from_current_date) + "-" + str(prev_month_2digit)

            payroll = Payroll.objects.filter(created_at__contains=current_month_year)
            if len(payroll) == 0:
                # EMPLOYEE LIST LOOP
                employee_list = Employee.objects.all()
                len_employee_list = len(employee_list)
                for x in range(len_employee_list):
                    # GET EMPLOYEE SALARY DETAIL
                    get_employee_code = employee_list[x].employee_code
                    get_employee_salary = EmployeeSalary.objects.get(employee_code_id=get_employee_code)
                    total_salary = 0
                    if get_employee_salary.pay_frequency == 'monthly':
                        total_salary = get_employee_salary.basic_salary
                    elif get_employee_salary.pay_frequency == 'daily':
                        hourly_rate = get_employee_salary.rate_amount
                        monthly_total_hour = int(8) * int(22)
                        total_salary = int(hourly_rate) * monthly_total_hour

                    # SUM EMPLOYEE MONTH ALLOWANCE
                    query_employee_allowance = "SELECT employee_code_id, sum(amount) as total  from (select allowance_amount as amount,employee_code_id, created_at from tbl_employee_allowance_fixed where created_at::CHARACTER VARYING like '%" + previous_month_year + "%' union all SELECT trans_amount as amount, employee_code_id, created_at from tbl_employee_allowance_trans where created_at::CHARACTER VARYING like '%" + previous_month_year + "%') t where employee_code_id = '" + get_employee_code + "' GROUP BY employee_code_id"
                    cursor.execute(query_employee_allowance)
                    employee_allowance = DictinctFetchAll(cursor)
                    if len(employee_allowance) > 0:
                        total_allowance = employee_allowance[0]['total']
                    else:
                        total_allowance = 0
                    # SUM EMPLOYEE MONTH DEDUCTION
                    query_employee_deduction = "SELECT employee_code_id, sum(amount) as total  from (select deduction_amount as amount,employee_code_id, created_at from tbl_employee_deduction_fixed where created_at::CHARACTER VARYING like '%" + previous_month_year + "%' union all SELECT trans_amount as amount, employee_code_id, created_at from tbl_employee_deduction_trans where created_at::CHARACTER VARYING like '%" + previous_month_year + "%') t where employee_code_id = '" + get_employee_code + "' GROUP BY employee_code_id"
                    cursor.execute(query_employee_deduction)
                    employee_deduction = DictinctFetchAll(cursor)
                    if len(employee_deduction) > 0:
                        total_deduction = employee_deduction[0]['total']
                    else:
                        total_deduction = 0

                    # GET PREVIOUS MONTH PAYROLL DETAIL
                    query_payrolls = "select * from tbl_employee_payroll where created_at::CHARACTER VARYING LIKE '%" + previous_month_year + "%' AND employee_code_id = '" + get_employee_code + "'"
                    cursor.execute(query_payrolls)
                    payroll_lists = DictinctFetchAll(cursor)
                    len_payroll_lists = len(payroll_lists)

                    prev_closing_balance = 0
                    if len_payroll_lists > 0:
                        prev_closing_balance = payroll_lists[0]['closing_bal']

                        # EMPLOYEE PAYABLE AMOUNT
                    payable_amount = (total_salary + total_allowance) - total_deduction + prev_closing_balance

                    get_auto_payroll_code = AutoGenerateCodeForModel(Payroll, "payroll_code", "PAYR-")
                    InstPayroll = Payroll()
                    InstPayroll.employee_code_id = get_employee_code
                    InstPayroll.payroll_code = get_auto_payroll_code
                    InstPayroll.pay_date = current_date
                    InstPayroll.basic_pay = total_salary
                    InstPayroll.allowances = total_allowance
                    InstPayroll.deduction = total_deduction
                    InstPayroll.status = "Unpaid"
                    InstPayroll.net_pay = payable_amount
                    InstPayroll.opening_bal = prev_closing_balance
                    InstPayroll.closing_bal = 0
                    InstPayroll.created_by = request.session['username']
                    InstPayroll.save()
                    message = "Success"
            else:
                message = "Error"

    btn_generated = "no"
    employee_payroll = Payroll.objects.filter(created_at__contains=current_month_year, status='Unpaid')
    if len(employee_payroll) == 0:
        btn_generated = "yes"

    query_employee_payroll = "select title, pay.employee_code_id as employee_code,payroll_code,  pay.created_at, pay.status, basic_pay, allowances, deduction, net_pay, opening_bal, closing_bal from tbl_employee_information empi INNER JOIN tbl_employee_payroll pay ON empi.employee_code_id = pay.employee_code_id  where pay.created_at::CHARACTER VARYING like '%" + current_month_year + "%' and pay.status = 'Unpaid'"
    cursor.execute(query_employee_payroll)
    employee_payroll = DictinctFetchAll(cursor)

    param = {
        'message': message,
        'employee_payroll': employee_payroll,
        'btn_generated': btn_generated,
    }
    return render(request, template_name, param)


@login_required(login_url='LoginView')
def PayrollStatementView(request):
    message = ""
    template_name = "Payroll/PayrollView.html"
    cursor = connections['default'].cursor()

    format_str = '%Y-%m-%d'
    date = datetime.datetime.now().strftime(format_str)
    # GET CURRENT MONTH AND YEAR
    d_part = date.split("-")
    get_year = d_part[0]
    get_month = d_part[1]
    get_location = "%"
    get_employee = "%"

    # GET ALL PAYROLL MONTH
    query_employee_payroll_month = "SELECT date_part('month', created_at::date)::INTEGER  AS month_number, to_char(created_at::date, 'Month') AS month_name FROM tbl_employee_payroll GROUP BY month_name , month_number"
    cursor.execute(query_employee_payroll_month)
    employee_payroll_month = DictinctFetchAll(cursor)
    # GET ALL PAYROLL YEAR
    query_employee_payroll_year = "SELECT date_part('year', created_at::date)::INTEGER AS year FROM tbl_employee_payroll GROUP BY year"
    cursor.execute(query_employee_payroll_year)
    employee_payroll_year = DictinctFetchAll(cursor)
    # GET ALL EMPLOYEE
    all_employee = list(EmployeeInformation.objects.all().values('title', 'employee_code_id'))
    # GET ALL EMPLOYEE LOCATIONS
    employee_location = list(LocationStore.objects.all().values())

    employee_payroll = ""
    if request.method == "POST":
        get_year = request.POST['year']
        get_month = request.POST['month']
        get_employee = request.POST['employee']
        get_location = request.POST['location']
        message = "Success" + "^" + get_year + "^" + get_month + "^" + get_employee + "^" + get_location

    if get_location == "%":
        query_employee_payroll = "select title, pay.employee_code_id as employee_code, payroll_code,  pay.created_at, pay.status, basic_pay, allowances, deduction, net_pay, opening_bal, closing_bal, date_part('year', pay.created_at::date)::INTEGER AS year, date_part('month', pay.created_at::date)::INTEGER  AS month_number from tbl_employee_information empi INNER JOIN tbl_employee_payroll pay ON empi.employee_code_id = pay.employee_code_id where date_part('year', pay.created_at::date)::CHARACTER VARYING  LIKE  '" + get_year + "' AND date_part('month', pay.created_at::date)::CHARACTER VARYING  LIKE  '" + get_month + "' AND pay.employee_code_id LIKE '" + get_employee + "'"
        cursor.execute(query_employee_payroll)
        employee_payroll = DictinctFetchAll(cursor)

    elif get_location != "%":
        query_employee_payroll = "select title, pay.employee_code_id as employee_code,loc_store_code_id, payroll_code,  pay.created_at, pay.status, basic_pay, allowances, deduction, net_pay, opening_bal, closing_bal, date_part('year', pay.created_at::date)::INTEGER AS year, date_part('month', pay.created_at::date)::INTEGER  AS month_number from tbl_employee_information empi INNER JOIN tbl_employee_payroll pay ON empi.employee_code_id = pay.employee_code_id INNER JOIN tbl_employee_location empl ON empi.employee_code_id = empl.employee_code_id where date_part('year', pay.created_at::date)::CHARACTER VARYING  LIKE  '" + get_year + "' AND date_part('month', pay.created_at::date)::CHARACTER VARYING  LIKE '" + get_month + "' AND pay.employee_code_id LIKE '" + get_employee + "' AND loc_store_code_id LIKE '" + get_location + "'"
        cursor.execute(query_employee_payroll)
        employee_payroll = DictinctFetchAll(cursor)

    param = {
        'message': message,
        'employee_payroll': employee_payroll,
        'month': employee_payroll_month,
        'year': employee_payroll_year,
        'all_employee': all_employee,
        'employee_location': employee_location,
    }
    return render(request, template_name, param)


def MakePayerollPaymentsView(request):
    message = ""
    get_payroll_code = request.POST['payroll_code']
    split_payroll_code = get_payroll_code.split(",")
    len_payroll_code = len(split_payroll_code)

    for i in range(len_payroll_code):
        employee = split_payroll_code[i]
        single_payroll_code = employee.strip(" '' ")
        InstPayroll = Payroll.objects.get(payroll_code=single_payroll_code)

        pay = InstPayroll.net_pay
        if pay > 0:
            balance = 0
        else:
            balance = pay

        InstPayroll.closing_bal = balance
        InstPayroll.status = "Paid"
        InstPayroll.save()
        message = "Success"

    return HttpResponse(json.dumps({'message': message}))


# PAYROLL VIEW (END)

@login_required(login_url='LoginView')
def UpdateMultipleEmployeeSalaryView(request):
    message = ""
    template_name = "Payroll/EmployeeSalary.html"
    cursor = connections['default'].cursor()
    # GET ALL EMPLOYEE
    all_employee = list(EmployeeInformation.objects.all().values('title', 'employee_code_id'))
    # GET ALL EMPLOYEE LOCATIONS
    employee_location = list(LocationStore.objects.all().values())
    # GET ALL POSITIONS
    all_positions = Position.objects.all()

    query_employee_salary = " SELECT salary_code, pay_frequency, rate_type, rate_amount, start_date ,basic_salary ,  title , emps.employee_code_id , loc_store_code_id FROM tbl_employee_salary emps INNER JOIN tbl_employee_information empi ON emps.employee_code_id = empi.employee_code_id INNER JOIN tbl_employee_location empl ON emps.employee_code_id = empl.employee_code_id INNER JOIN tbl_employee emp ON emps.employee_code_id = emp.employee_code where emps.employee_code_id like '%' and loc_store_code_id like '%'  and position_code_id like '%'"
    cursor.execute(query_employee_salary)
    employee_salary = DictinctFetchAll(cursor)

    if request.method == "POST":
        get_employee = request.POST['employee']
        get_location = request.POST['location']
        get_position = request.POST['position']
        message = "Success" + "^" + get_location + "^" + get_employee + "^" + get_position

        if get_location == '%':
            query_employee_salary = "SELECT salary_code, pay_frequency, rate_type, rate_amount, start_date ,basic_salary ,  title , emps.employee_code_id, position_code_id  FROM tbl_employee_salary emps INNER JOIN tbl_employee_information empi ON emps.employee_code_id = empi.employee_code_id INNER JOIN tbl_employee emp ON emps.employee_code_id = emp.employee_code where emps.employee_code_id like '" + get_employee + "' and position_code_id like '" + get_position + "'"
            cursor.execute(query_employee_salary)
            employee_salary = DictinctFetchAll(cursor)
        else:
            query_employee_salary = " SELECT salary_code, pay_frequency, rate_type, rate_amount, start_date ,basic_salary ,  title , emps.employee_code_id , loc_store_code_id FROM tbl_employee_salary emps INNER JOIN tbl_employee_information empi ON emps.employee_code_id = empi.employee_code_id INNER JOIN tbl_employee_location empl ON emps.employee_code_id = empl.employee_code_id INNER JOIN tbl_employee emp ON emps.employee_code_id = emp.employee_code where emps.employee_code_id like '" + get_employee + "' and loc_store_code_id like '" + get_location + "'  and position_code_id like '" + get_position + "'"
            cursor.execute(query_employee_salary)
            employee_salary = DictinctFetchAll(cursor)

    param = {
        'message': message,
        'employee_salary': employee_salary,
        'all_employee': all_employee,
        'employee_location': employee_location,
        'all_positions': all_positions,
    }
    return render(request, template_name, param)


# LEAVE VIEW START
@login_required(login_url='LoginView')
def NationalHolidayView(request):
    message = ""
    template_name = "Leave/Holiday.html"
    holiday_list = Holiday.objects.all().order_by('id')
    params = {'holiday_list': holiday_list}
    return render(request, template_name, params)


@login_required(login_url='LoginView')
def AddNationalHolidayView(request):
    message = ""

    get_action_type = request.POST['action_type']
    get_holiday_id = request.POST['holiday_id']
    get_holiday_name = request.POST['holiday_name']
    get_holiday_date = request.POST['holiday_date']
    get_holiday_description = request.POST['holiday_description']
    dateTime = datetime.datetime.now()

    if get_action_type == 'NEW':
        holiday_auto_generate = AutoGenerateCodeForModel(Holiday, "holiday_code", "HOLI-")
        key_holiday_code = get_holiday_name.strip()
        InstEmpHoliday = Holiday(
            holiday_code=holiday_auto_generate,
            holiday_name=key_holiday_code,
            holiday_date=get_holiday_date,
            description=get_holiday_description,
            created_at=dateTime,
            created_by=request.session['username'],
        )
        InstEmpHoliday.save()
        message = "Success"

    elif get_action_type == 'UPDATE':
        key_holiday_code = get_holiday_name.strip()
        UpdateHoliday = Holiday.objects.get(id=get_holiday_id)
        UpdateHoliday.holiday_name = key_holiday_code
        UpdateHoliday.holiday_date = get_holiday_date
        UpdateHoliday.description = get_holiday_description
        UpdateHoliday.updated_at = dateTime
        UpdateHoliday.updated_by = request.session['username']
        UpdateHoliday.save()
        message = "Success"

    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def DeleteNationalHolidayView(request):
    message = ""
    get_id = request.POST['id']

    delete_Holiday = Holiday.objects.get(id=get_id)
    delete_Holiday.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def WeeklyWorkingView(request):
    message = ""
    template_name = "Leave/WeeklyWorking.html"
    # WeeklyWorking_list = WeeklyWorking.objects.all().order_by('id')
    # params = {'WeeklyWorking_list': WeeklyWorking_list}

    return render(request, template_name)


@login_required(login_url='LoginView')
def AddWeeklyWorkingView(request):
    message = ""

    get_action_type = request.POST['action_type']
    get_weekly_id = request.POST['weekly_id']
    get_schedule_code = request.POST['cmd_schedule_id']
    get_weekly_dayname = request.POST['weekly_dayname']
    get_start_time = request.POST['start_time']
    get_end_time = request.POST['end_time']

    dateTime = datetime.datetime.now()

    # if get_action_type == 'NEW':
    #     week_work_auto_generate = AutoGenerateCodeForModel(WeeklyWorking, "work_code", "WORK-")
    #     InstWeeklyWorking = WeeklyWorking(
    #         work_code=week_work_auto_generate,
    #         sche_code_id=get_schedule_code,
    #         day_name=get_weekly_dayname,
    #         start_time=get_start_time,
    #         end_time=get_end_time,
    #         created_at=dateTime,
    #         created_by=request.session['username'],
    #     )
    #     InstWeeklyWorking.save()
    #     message = "Success"
    #
    # elif get_action_type == 'UPDATE':
    #     UpdateWeeklyWorking = WeeklyWorking.objects.get(id=get_weekly_id)
    #     UpdateWeeklyWorking.sche_code_id = get_schedule_code
    #     UpdateWeeklyWorking.day_name = get_weekly_dayname
    #     UpdateWeeklyWorking.start_time = get_start_time
    #     UpdateWeeklyWorking.end_time = get_end_time
    #     UpdateWeeklyWorking.updated_at = dateTime
    #     UpdateWeeklyWorking.updated_by = request.session['username']
    #     UpdateWeeklyWorking.save()
    #     message = "Success"

    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def DeleteWeeklyWorkingView(request):
    message = ""
    get_id = request.POST['id']

    # delete_Weekly_Working = WeeklyWorking.objects.get(id=get_id)
    # delete_Weekly_Working.delete()
    message = "Success"

    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def LeaveTypeView(request):
    message = ""
    template_name = "Leave/LeaveType.html"
    Leave_type_list = LeaveType.objects.all().order_by('id')
    params = {'Leave_type_list': Leave_type_list}
    return render(request, template_name, params)


@login_required(login_url='LoginView')
def AddLeaveTypeView(request):
    message = ""

    get_action_type = request.POST['action_type']
    get_leave_type_id = request.POST['leave_type_id']
    get_leave_type_name = request.POST['leave_type_name']
    dateTime = datetime.datetime.now()

    if get_action_type == 'NEW':
        leave_auto_generate = AutoGenerateCodeForModel(LeaveType, "leave_type_code", "LTP-")
        key_leave_code = get_leave_type_name.strip()
        InstEmpLeaveType = LeaveType(
            leave_type_code=leave_auto_generate,
            leave_type_name=key_leave_code,
            status="Active",
            created_at=dateTime,
            created_by=request.session['username'],
        )
        InstEmpLeaveType.save()
        message = "Success"

    elif get_action_type == 'UPDATE':
        key_leave_code = get_leave_type_name.strip()
        UpdateLeaveType = LeaveType.objects.get(id=get_leave_type_id)
        UpdateLeaveType.leave_type_name = key_leave_code
        UpdateLeaveType.updated_at = dateTime
        UpdateLeaveType.updated_by = request.session['username']
        UpdateLeaveType.save()
        message = "Success"

    return HttpResponse(json.dumps({'message': message}))


@login_required(login_url='LoginView')
def DeleteLeaveTypeView(request):
    message = ""
    get_id = request.POST['id']

    delete_leave = LeaveType.objects.get(id=get_id)
    delete_leave.delete()
    message = "Success"
    return HttpResponse(json.dumps({'message': message}))


# SHOW FIXED TYPE DEDUCTION
@login_required(login_url='LoginView')
def FillCmdDeductionTypeNameView(request):
    deduction_type = list(DeductionType.objects.filter(type='fixed').values())
    param = {
        'cmd_list': deduction_type
    }
    return HttpResponse(json.dumps(param, default=date_handler))


# SHOW NON FIXED TYPE DEDUCTION
@login_required(login_url='LoginView')
def FillCmdNonDeductionTypeNameView(request):
    deduction_type = list(DeductionType.objects.filter(type='non-fixed').values())
    param = {
        'cmd_list': deduction_type
    }
    return HttpResponse(json.dumps(param, default=date_handler))


# SHOW FIXED TYPE ALLOWANCE
@login_required(login_url='LoginView')
def FillCmdFixedAllowanceTypeNameView(request):
    allowance_type = list(AllowanceType.objects.filter(type='fixed').values())
    param = {
        'cmd_list': allowance_type
    }
    return HttpResponse(json.dumps(param, default=date_handler))


# SHOW NON FIXED TYPE ALLOWANCE
@login_required(login_url='LoginView')
def FillCmdNonAllowanceTypeNameView(request):
    allowance_type = list(AllowanceType.objects.filter(type='non-fixed').values())
    param = {
        'cmd_list': allowance_type
    }
    return HttpResponse(json.dumps(param, default=date_handler))

# LEAVE VIEW END

# Attendance View:

# @login_required(login_url='LoginView')
# def AttendanceView(request):
#     # get_code = code
#     template_name = "Employee/Attendance.html"
#
#     cursor = connections['default'].cursor()
#
#     Emp_list = Employee.objects.all().order_by('id')
#     emp_attendance = EmployeeAttendance.objects.all().order_by('id')
#     # emp_attendance_list = list(EmployeeAttendance.objects.filter(emp_attendance_code=get_code))[0]
#
#     format_str = '%Y-%m-%d'
#     date = datetime.datetime.now().strftime(format_str)
#     d_part = date.split("-")
#
#     current_day = int(d_part[2])
#
#     day_hierarchy_header = []
#     count = 1
#     for data in range(current_day):
#         day_hierarchy_header.append(count)
#         count += 1
#
#     start_date = datetime.date(int(d_part[0]), int(d_part[1]), int(d_part[2]))
#     month_start_date = start_date.replace(day=1)
#     month_end_date = datetime.date(int(d_part[0]), int(d_part[1]), int(d_part[2]))
#
#     # ATTENDANCE DETAIL
#     query_employee_att = "SELECT employee_code, COALESCE(check_in, 'NA') AS check_in, COALESCE(check_out, 'NA') AS check_out FROM tbl_employee emp LEFT OUTER JOIN (SELECT employee_code_id, check_in, check_out FROM tbl_employee_attendance GROUP BY employee_code_id, check_in, check_out) emp_att ON emp.employee_code = emp_att.employee_code_id ORDER BY id"
#     cursor.execute(query_employee_att)
#     emp_att_list = DictinctFetchAll(cursor)
#
#     params = {'emp_att_list': emp_att_list,
#               'day_hierarchy_header': day_hierarchy_header,
#               'Emp_list': Emp_list,
#               'emp_attendance': emp_attendance
#               }
#
#     return render(request, template_name, params)
#
#
# # Add Attendance View:
#
# @login_required(login_url='LoginView')
# def AddAttendanceView(request):
#     message = ""
#     get_action_type = request.POST['action_type']
#     get_emp_id = request.POST['emp_id']
#     get_check_in = request.POST['check_in']
#     get_check_out = request.POST['check_out']
#
#     dateTime = datetime.datetime.now()
#
#     format_str = '%Y-%m-%d'
#     date = datetime.datetime.now().strftime(format_str)
#     d_part = date.split("-")
#
#     if get_action_type == 'NEW':
#         # filter
#         Emp_Attn = EmployeeAttendance.objects.filter(employee_code=get_emp_id)
#         EmpAttLength = len(Emp_Attn)
#         # or length 0 insert
#         if EmpAttLength == 0:
#             attendance_auto_generate = AutoGenerateCodeForModel(EmployeeAttendance, "emp_attendance_code", "EA-")
#             InstEmpAttendance = EmployeeAttendance(
#                 emp_attendance_code=attendance_auto_generate,
#                 employee_code_id=get_emp_id,
#                 check_in=get_check_in,
#                 check_out=get_check_out,
#                 status="Present",
#                 created_at=datetime,
#                 created_by=request.session['username'],
#             )
#             InstEmpAttendance.save()
#             message = "Success"
#         # more than 1 update`
#         else:
#             EmpAttTime = EmployeeAttendance.objects.get(employee_code=get_emp_id)
#             EmpAttTime.check_in = get_check_in
#             EmpAttTime.check_out = get_check_out
#             EmpAttTime.save()
#             message = "Success"
#
#         message = "Success"
#         # employee_code and current_date get
#
#     elif get_action_type == 'UPDATE':
#         UpdateEmpAtt = EmployeeAttendance.objects.get(employee_code=get_emp_id)
#         UpdateEmpAtt.check_in = get_check_in
#         UpdateEmpAtt.check_out = get_check_out
#         UpdateEmpAtt.updated_at = dateTime
#         UpdateEmpAtt.updated_by = request.session['username']
#         UpdateEmpAtt.save()
#         message = "Success"
#
#     return HttpResponse(json.dumps({'message': message}))
