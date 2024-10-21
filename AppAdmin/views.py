import json
import datetime
#
from django.contrib.auth.decorators import login_required
#
from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render
#
from AppAdmin.models import *
from AppAdmin.utils import *
# from AppPurchase.models import *
from AppAdmin.forms import *
# from AppChartAccount.models import *
from django.db.models import Sum
import os


# # Create your views here.
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else str(obj)
#
#
# @login_required(login_url='LoginView')
# def attendanceView(request):
#     template_name = "AdminSetting/Wharehouse.html"
#
#     po = PurchaseOrder.objects.all()
#     # Aggregate give us dict
#     grand_total = po.aggregate(total=Sum('grand_total'))
#     # Values() give us dict
#     grand_total_value = PurchaseOrder.objects.values("grand_total")
#
#     total = PurchaseOrder.objects.values("grand_total").annotate(Sum('grand_total'))
#
#
#     raw_query = PurchaseOrder.objects.raw('SELECT id, grand_total,ex_total_amount, gst_total_amount FROM tbl_purchase_order')
#
#     po1 = PurchaseOrder.objects.select_related('supplier_code')
#
#
#     return render(request, template_name)
#
#
@login_required(login_url='LoginView')
def DashboardView(request):
    template_name = "Dashboard.html"

    return render(request, template_name)

#
# @login_required(login_url='LoginView')
# def PaymentMethodView(request):
#     template_name = "AdminSetting/PaymentMethod.html"
#
#     payment_list = PaymentMethod.objects.all().order_by('pm_name')
#     params = {'payment_list': payment_list}
#     return render(request, template_name, params)
#
#
# @login_required(login_url='LoginView')
# def AddPaymentMethodView(request):
#     message = ""
#     get_action_type = request.POST['action_type']
#     get_pm_code = request.POST['pm_code']
#     get_pm_name = request.POST['pm_name']
#     dateTime = datetime.datetime.now()
#
#     if get_action_type == "NEW":
#
#         pm_auto_code = AutoGenerateCodeForModel(PaymentMethod, "pm_code", "PM-")
#         key_pm_name = get_pm_name.strip()
#         InstPayment = PaymentMethod(
#             pm_code=pm_auto_code,
#             pm_name=key_pm_name,
#             status="Active",
#             created_at=dateTime,
#             created_by=request.session['username'],
#         )
#         InstPayment.save()
#         message = "Success"
#
#     elif get_action_type == "UPDATE":
#         key_pm_name = get_pm_name.strip()
#         UpdatePayment = PaymentMethod.objects.get(id=get_pm_code)
#         UpdatePayment.pm_name = key_pm_name
#         UpdatePayment.updated_at = dateTime
#         UpdatePayment.updated_by = request.session['username']
#         UpdatePayment.save()
#         message = "Update"
#
#     return HttpResponse(json.dumps({'message': message}))
#
#
# @login_required(login_url='LoginView')
# def DeletePaymentMethodView(request):
#     message = ""
#     get_id = request.POST['id']
#     delete_category = PaymentMethod.objects.get(id=get_id)
#     delete_category.delete()
#     message = "Success"
#     return HttpResponse(json.dumps({'message': message}))
#
#
@login_required(login_url='LoginView')
def FillCmdPaymentMethodView(request):
    payment_method_list = list(PaymentMethod.objects.values('pm_code', 'pm_name').order_by('pm_name'))
    return HttpResponse(json.dumps({'cmd_list': payment_method_list}))

#
# @login_required(login_url='LoginView')
# def FillCmdEmployeePaymentMethodView(request):
#     get_employee_code = request.POST['employee_code']
#
#     cursor = connections['default'].cursor()
#     query_employee = "select payment_code as pm_code, pm_name , account_number , bank_name from tbl_payment_method pm INNER JOIN tbl_employee_payment_method epm ON pm.pm_code = epm.pm_code_id left JOIN tbl_bank_data bank ON epm.bank_code_id = bank.bank_code where employee_code_id = '" + get_employee_code + "'"
#     cursor.execute(query_employee)
#     employee_payment_method = DictinctFetchAll(cursor)
#
#     # employee_payment_method = list(EmployeePaymentMethod.objects.values('pm_code', 'pm_name').order_by('pm_name'))
#     return HttpResponse(json.dumps({'cmd_list': employee_payment_method}))
#
#
# @login_required(login_url='LoginView')
# def BankListView(request):
#     template_name = "AdminSetting/BankList.html"
#     bank_list = BankData.objects.all().order_by('id')
#     params = {'bank_list': bank_list}
#     return render(request, template_name, params)
#
#
# @login_required(login_url='LoginView')
# def AddNewBankview(request):
#     message = ""
#     get_action_type = request.POST['action_type']
#     get_bank_id = request.POST['bank_id']
#     get_bank_name = request.POST['bank_name']
#     get_bank_code = request.POST['bank_code']
#     dateTime = datetime.datetime.now()
#
#     if get_action_type == "NEW":
#
#         key_bank_name = get_bank_name.strip()
#         key_bank_code = get_bank_code.strip()
#         Instbank = BankData(
#             bank_name=key_bank_name,
#             bank_code=key_bank_code,
#             status="Active",
#             created_at=dateTime,
#             created_by=request.session['username'],
#         )
#         Instbank.save()
#         message = "Success"
#
#     elif get_action_type == "UPDATE":
#         key_bank_name = get_bank_name.strip()
#         key_bank_code = get_bank_code.strip()
#         UpdateBank = BankData.objects.get(id=get_bank_id)
#         UpdateBank.bank_name = key_bank_name
#         UpdateBank.bank_code = key_bank_code
#         UpdateBank.updated_at = dateTime
#         UpdateBank.updated_by = request.session['username']
#         UpdateBank.save()
#         message = "Success"
#
#     return HttpResponse(json.dumps({'message': message}))
#
#
# @login_required(login_url='LoginView')
# def DeleteBankView(request):
#     message = ""
#     get_id = request.POST['id']
#     delete_bank = BankData.objects.get(id=get_id)
#     delete_bank.delete()
#     message = "Success"
#     return HttpResponse(json.dumps({'message': message}))
#
#
# # SEGMENT VIEW START
# @login_required(login_url='LoginView')
# def CompanyView(request):
#     template_name = "Segments/Company/Company.html"
#     company_list = Company.objects.all().order_by("company_name")
#     param = {
#         'company_list': company_list
#     }
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def AddCompanyView(request):
#     message = ""
#     template_name = "Segments/Company/AddCompany.html"
#     form = FormCompany()
#     if request.method == "POST":
#         form_class = FormCompany(request.POST, request.FILES)
#         if form_class.is_valid():
#             get_form_inst = form_class.save(commit=False)
#             get_form_inst.status = "Active"
#             get_form_inst.created_at = datetime.datetime.now()
#             get_form_inst.created_by = request.session['username']
#             get_form_inst.save()
#             message = "Success"
#     else:
#         form = FormCompany()
#         message = "Error"
#
#     params = {'form': form,
#               'message': message}
#     return render(request, template_name, params)
#
#
# @login_required(login_url='LoginView')
# def UpdateCompanyView(request, code):
#     get_company_code = code
#     message = ""
#     template_name = "Segments/Company/UpdateCompany.html"
#     form = FormCompany()
#     if request.method == "POST":
#         company = Company.objects.get(company_code=code)
#         if company.image:
#             if os.path.isfile(company.image.path):
#                 os.remove(company.image.path)
#
#         company_inst = Company.objects.get(company_code=get_company_code)
#         company_inst_form = FormCompany(request.POST, request.FILES, instance=company_inst)
#         get_form_company = company_inst_form.save(commit=False)
#
#         get_form_company.company_code = get_company_code
#         get_form_company.updated_at = datetime.datetime.now()
#         get_form_company.updated_by = request.session['username']
#
#         get_form_company.save()
#
#         message = "Success"
#
#     else:
#         form = FormCompany()
#         message = "Error"
#
#     company_list = list(Company.objects.filter(company_code=get_company_code).order_by('company_name'))[0]
#
#     params = {'form': form,
#               'company_list': company_list,
#               'message': message}
#
#     return render(request, template_name, params)
#
#
# @login_required(login_url='LoginView')
# def LineBusinessView(request):
#     template_name = "Segments/LineBusiness.html"
#     Line_Business = LineBusiness.objects.all().order_by('line_bus_name')
#     param = {
#         'Line_Business': Line_Business
#     }
#     return render(request, template_name, param)
#
#
# def AddLineBusinessView(request):
#     message = ""
#     get_action_type = request.POST['action_type']
#     get_ids = request.POST['get_id']
#     get_line_buss_code = request.POST['line_buss_code']
#     get_line_buss_name = request.POST['line_buss_name']
#     dateTime = datetime.datetime.now()
#
#     if get_action_type == "NEW":
#
#         key_line_buss_name = get_line_buss_name.strip()
#
#         InstLineBussiness = LineBusiness(
#             line_bus_code=get_line_buss_code,
#             line_bus_name=key_line_buss_name,
#             status="Active",
#             created_at=dateTime,
#             created_by=request.session['username']
#         )
#         InstLineBussiness.save()
#         message = "Success"
#
#     elif get_action_type == "UPDATE":
#
#         key_line_buss_name = get_line_buss_name.strip()
#         UpdateLineBusiness = LineBusiness.objects.get(id=get_ids)
#         UpdateLineBusiness.line_bus_code = get_line_buss_code
#         UpdateLineBusiness.line_bus_name = key_line_buss_name
#         UpdateLineBusiness.updated_at = dateTime
#         UpdateLineBusiness.updated_by = request.session['username']
#         UpdateLineBusiness.save()
#         message = "Success"
#
#     return HttpResponse(json.dumps({'message': message}))
#
#
# def DeleteLineBussiness(request):
#     message = ""
#     get_id = request.POST['id']
#     delete_line_bussiness = LineBusiness.objects.get(id=get_id)
#     delete_line_bussiness.delete()
#     message = "Success"
#     return HttpResponse(json.dumps({'message': message}))
#
#
# @login_required(login_url='LoginView')
# def BusinessSectorView(request):
#     template_name = "Segments/BusinessSector.html"
#     Business_sector = BusinessSector.objects.all().order_by('bus_sect_name')
#     param = {
#         'Business_sector': Business_sector
#     }
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def AddBusinessSectorView(request):
#     message = ""
#     get_action_type = request.POST['action_type']
#     get_ids = request.POST['get_id']
#     get_buss_sect_code = request.POST['buss_sect_code']
#     get_buss_sect_name = request.POST['buss_sect_name']
#     dateTime = datetime.datetime.now()
#
#     if get_action_type == "NEW":
#
#         key_get_buss_sect_name = get_buss_sect_name.strip()
#
#         InstBusinessSctor = BusinessSector(
#             bus_sect_code=get_buss_sect_code,
#             bus_sect_name=key_get_buss_sect_name,
#             status="Active",
#             created_at=dateTime,
#             created_by=request.session['username']
#         )
#         InstBusinessSctor.save()
#         message = "Success"
#
#     elif get_action_type == "UPDATE":
#         key_get_buss_sect_name = get_buss_sect_name.strip()
#         UpdateBusinessSector = BusinessSector.objects.get(id=get_ids)
#         UpdateBusinessSector.bus_sect_code = get_buss_sect_code
#         UpdateBusinessSector.bus_sect_name = key_get_buss_sect_name
#         UpdateBusinessSector.updated_at = dateTime
#         UpdateBusinessSector.updated_by = request.session['username']
#         UpdateBusinessSector.save()
#         message = "Success"
#
#     return HttpResponse(json.dumps({'message': message}))
#
#
# @login_required(login_url='LoginView')
# def DeleteBussinessSector(request):
#     message = ""
#     get_id = request.POST['id']
#     delete_bussiness_sector = BusinessSector.objects.get(id=get_id)
#     delete_bussiness_sector.delete()
#     message = "Success"
#     return HttpResponse(json.dumps({'message': message}))
#
#
# @login_required(login_url='LoginView')
# def CostCenterView(request):
#     template_name = "Segments/CostCenter.html"
#     Cost_Center = CostCenter.objects.all().order_by('cost_center_name')
#     param = {
#         'Cost_Center': Cost_Center
#     }
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def AddCostCenterView(request):
#     message = ""
#     get_action_type = request.POST['action_type']
#     get_center_code = request.POST['cost_center_code']
#     get_center_name = request.POST['cost_center_name']
#     dateTime = datetime.datetime.now()
#
#     if get_action_type == "NEW":
#
#         key_get_center_name = get_center_name.strip()
#         center_auto_code = AutoGenerateNumberCodeForModel(CostCenter, "cost_center_code")
#
#         InstCostCenter = CostCenter(
#             cost_center_code=center_auto_code,
#             cost_center_name=key_get_center_name,
#             status="Active",
#             created_at=dateTime,
#             created_by=request.session['username']
#         )
#         InstCostCenter.save()
#         message = "Success"
#
#     elif get_action_type == "UPDATE":
#         key_get_center_name = get_center_name.strip()
#         UpdateCostCenter = CostCenter.objects.get(cost_center_code=get_center_code)
#         UpdateCostCenter.cost_center_name = key_get_center_name
#         UpdateCostCenter.updated_at = dateTime
#         UpdateCostCenter.updated_by = request.session['username']
#         UpdateCostCenter.save()
#         message = "Success"
#
#     return HttpResponse(json.dumps({'message': message}))
#
#
# @login_required(login_url='LoginView')
# def NaturalAccountView(request):
#     template_name = "Segments/NaturalAccount.html"
#     message = ""
#
#     # category_list = ChartAccountCategory.objects.all().order_by('category_name')
#     parent_list = ChartAccountParent.objects.all().order_by('parent_name')
#     sub_parent_list = ChartAccountSubParent.objects.all().order_by('sub_parent_name')
#     Child_list = ChartAccountChild.objects.all().order_by('child_name')
#
#     param = {
#         'parent_list': parent_list,
#         'sub_parent_list': sub_parent_list,
#         'Child_list': Child_list,
#         'message': message
#     }
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def LocationDataView(request):
#     template_name = "Segments/Location/LocationData.html"
#
#     location_data = LocationData.objects.all().order_by('loc_name')
#     param = {
#         'location_data': location_data
#     }
#
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def AddLocationDataView(request):
#     message = ""
#     get_action_type = request.POST['action_type']
#     get_loc_code = request.POST['loc_code']
#     get_loc_name = request.POST['loc_name']
#     dateTime = datetime.datetime.now()
#
#     if get_action_type == "NEW":
#         center_auto_code = AutoGenerateSingleDigitNumberCodeForModel(LocationData, "loc_code")
#
#         key_get_loc_name = get_loc_name.strip()
#
#         InstLocationData = LocationData(
#             loc_code=center_auto_code,
#             loc_name=key_get_loc_name,
#             status="Active",
#             created_at=dateTime,
#             created_by=request.session['username']
#         )
#         InstLocationData.save()
#         message = "Success"
#
#     elif get_action_type == "UPDATE":
#         key_get_loc_name = get_loc_name.strip()
#         UpdateLocationData = LocationData.objects.get(loc_code=get_loc_code)
#         UpdateLocationData.loc_name = key_get_loc_name
#         UpdateLocationData.updated_at = dateTime
#         UpdateLocationData.updated_by = request.session['username']
#         UpdateLocationData.save()
#         message = "Success"
#
#     return HttpResponse(json.dumps({'message': message}))
#
#
# @login_required(login_url='LoginView')
# def LocationCityView(request):
#     template_name = "Segments/Location/LocationCity.html"
#     location_city = LocationCity.objects.all().order_by('city_name')
#     param = {
#         'location_city': location_city
#     }
#
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def AddLocationCityView(request):
#     message = ""
#     get_action_type = request.POST['action_type']
#     get_city_code = request.POST['city_code']
#     get_city_name = request.POST['city_name']
#     dateTime = datetime.datetime.now()
#
#     if get_action_type == "NEW":
#         city_auto_code = AutoGenerateNumberCodeForModel(LocationCity, "city_code")
#
#         key_get_city_name = get_city_name.strip()
#
#         InstLocationCity = LocationCity(
#             city_code=city_auto_code,
#             city_name=key_get_city_name,
#             status="Active",
#             created_at=dateTime,
#             created_by=request.session['username']
#         )
#         InstLocationCity.save()
#         message = "Success"
#
#     elif get_action_type == "UPDATE":
#         key_get_city_name = get_city_name.strip()
#         UpdateLocationCity = LocationCity.objects.get(city_code=get_city_code)
#         UpdateLocationCity.city_name = key_get_city_name
#         UpdateLocationCity.updated_at = dateTime
#         UpdateLocationCity.updated_by = request.session['username']
#         UpdateLocationCity.save()
#         message = "Success"
#
#     return HttpResponse(json.dumps({'message': message}))
#
#
# @login_required(login_url='LoginView')
# def LocationStoreView(request):
#     template_name = "Segments/Location/LocationStore.html"
#
#     store_list = LocationStore.objects.all().order_by('loc_store_name')
#     param = {
#         'store_list': store_list
#     }
#
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def LocationStoreCombineCodeView(request):
#     message = ""
#     get_location_data = request.POST['get_location_data']
#     get_location_city = request.POST['get_location_city']
#
#     FetchLocationStore = LocationStore.objects.filter(loc_code_id=get_location_data)
#     LenFetchLocationStore = len(FetchLocationStore)
#
#     if LenFetchLocationStore == 0:
#         loc_first_code = '{0:03}'.format(1)  # 001
#         combine_code = get_location_data + get_location_city + loc_first_code
#     else:
#         Fetch_latest_record = FetchLocationStore.latest('loc_store_code')
#         get_latest_code = Fetch_latest_record.loc_store_code
#         split_latest_record = get_latest_code.split("^")
#         letter = [x for x in split_latest_record[0]]
#         remove_letters = letter[3:]
#         join_split = ''.join(remove_letters)
#         increment = int(join_split) + 1
#         format_increment = '{0:03}'.format(increment)
#         combine_code = get_location_data + get_location_city + str(format_increment)
#     message = "Success"
#     params = {'combine_code': combine_code,
#               'message': message,
#
#               }
#     return HttpResponse(json.dumps(params))
#
#
# @login_required(login_url='LoginView')
# def AddLocationStoreView(request):
#     message = ""
#     template_name = "Segments/Location/AddLocationStore.html"
#
#     form = FormLocationStore()
#     if request.method == "POST":
#         form_class = FormLocationStore(request.POST, request.FILES)
#         if form_class.is_valid():
#             get_form_inst = form_class.save(commit=False)
#
#             get_company = request.POST['cmd_company']
#             get_Line_business = request.POST['cmd_lob']
#             get_business_sector = request.POST['cmd_bs']
#             get_location_data = request.POST['cmd_location_data']
#             get_location_city = request.POST['cmd_location_city']
#
#             FetchLocationStore = LocationStore.objects.filter(loc_code_id=get_location_data)
#             LenFetchLocationStore = len(FetchLocationStore)
#
#             if LenFetchLocationStore == 0:
#                 loc_first_code = '{0:03}'.format(1)  # 001
#                 combine_code = get_location_data + get_location_city + loc_first_code
#             else:
#                 Fetch_latest_record = FetchLocationStore.latest('loc_store_code')
#                 get_latest_code = Fetch_latest_record.loc_store_code
#                 split_latest_record = get_latest_code.split("^")
#                 letter = [x for x in split_latest_record[0]]
#                 remove_letters = letter[3:]
#                 join_split = ''.join(remove_letters)
#                 increment = int(join_split) + 1
#                 format_increment = '{0:03}'.format(increment)
#                 combine_code = get_location_data + get_location_city + str(format_increment)
#
#             get_form_inst.loc_store_code = combine_code
#             get_form_inst.company_code_id = get_company
#             get_form_inst.line_bus_code_id = get_Line_business
#             get_form_inst.bus_sect_code_id = get_business_sector
#             get_form_inst.loc_code_id = get_location_data
#             get_form_inst.city_code_id = get_location_city
#             get_form_inst.status = "Active"
#             get_form_inst.created_at = datetime.datetime.now()
#             get_form_inst.created_by = request.session['username']
#             get_form_inst.save()
#             message = "Success"
#     else:
#         form = FormLocationStore()
#         message = "Error"
#
#     Company_list = Company.objects.all().order_by('company_name')
#     lob_list = LineBusiness.objects.all().order_by('line_bus_name')
#     bs_list = BusinessSector.objects.all().order_by('bus_sect_name')
#     center_list = CostCenter.objects.all().order_by('cost_center_name')
#     loc_data_list = LocationData.objects.all().order_by('loc_name')
#     loc_city_list = LocationCity.objects.all().order_by('city_name')
#
#     params = {'form': form,
#               'message': message,
#               'Company_list': Company_list,
#               'lob_list': lob_list,
#               'bs_list': bs_list,
#               'center_list': center_list,
#               'loc_data_list': loc_data_list,
#               'loc_city_list': loc_city_list
#               }
#
#     return render(request, template_name, params)
#
#
# @login_required(login_url='LoginView')
# def BusinessBankView(request):
#     template_name = "BusinessBank/BusinessBank.html"
#     business_bank = BusinessAccount.objects.all()
#     param = {
#         'business_bank': business_bank
#     }
#
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def AddBusinessBankView(request):
#     message = ''
#     template_name = "BusinessBank/AddBusinessBank.html"
#     dateTime = datetime.datetime.now()
#
#     ## GET LATEST CHILD CODE
#     get_latest_child_code = ChartAccountChild.objects.filter(sub_parent_code_id='30110000').latest('child_code')
#     incerement_in_child_code = '{0:04}'.format(int(get_latest_child_code.child_code[-4:]) + 1)
#     latest_child_code = get_latest_child_code.child_code[:4] + incerement_in_child_code
#
#     busi_auto_code = AutoGenerateCodeForModel(BusinessAccount, "busi_acc_code", "BB-")
#
#     if request.method == 'POST':
#         get_city = request.POST['cmd_city']
#         get_state = request.POST['cmd_state']
#         get_address = request.POST['address']
#         get_country = request.POST['cmd_country']
#         get_status = request.POST['status']
#         get_location = request.POST['location']
#         get_account_title = request.POST['account_title']
#         get_account_no = request.POST['account_no']
#         get_ibn_number = request.POST['ibn_number']
#         get_branch_code = request.POST['branch_code']
#         get_activation_date = request.POST['activation_date']
#         get_block_date = request.POST['block_date']
#         get_description = request.POST['description']
#         coa_description = ''
#         if get_account_no != "":
#             coa_description = get_branch_code + ',' + get_account_no
#
#
#         ## ADD Bussiness Bank IN COA STOCK
#         coa_child = ChartAccountChild(
#             sub_parent_code_id='30110000',
#             child_code=latest_child_code,
#             child_name=get_account_title,
#             status='Active',
#             type='Bank',
#             description=coa_description,
#             created_at=dateTime,
#             created_by=request.session['username']
#
#         )
#         coa_child.save()
#
#         business_bank = BusinessAccount(
#             busi_acc_code=busi_auto_code,
#             account_title=get_account_title,
#             account_no=get_account_no,
#             branch_code=get_branch_code,
#             address=get_address,
#             city=get_city,
#             state=get_state,
#             country=get_country,
#             activation_date=get_activation_date,
#             block_date=get_block_date,
#             ibn_number=get_ibn_number,
#             description=get_description,
#             status=get_status,
#             loc_store_code_id=get_location,
#             child_code_id=latest_child_code,
#         )
#         business_bank.save()
#         incerement_in_child_code = '{0:04}'.format(int(get_latest_child_code.child_code[-4:]) + 2)
#         latest_child_code = get_latest_child_code.child_code[:4] + incerement_in_child_code
#         busi_auto_code = AutoGenerateCodeForModel(BusinessAccount, "busi_acc_code", "BB-")
#         message = "Success"
#
#     location_store = LocationStore.objects.all()
#
#     param = {
#         'location_store': location_store,
#         'message': message,
#         'latest_child_code': latest_child_code,
#         'busi_auto_code': busi_auto_code,
#     }
#
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def UpdateBusinessBankView(request, code):
#     get_busi_code = code
#     template_name = "BusinessBank/UpdateBusinessBank.html"
#     business_bank = BusinessAccount.objects.get(busi_acc_code=get_busi_code)
#
#     if request.method == 'POST':
#         get_city = request.POST['cmd_city']
#         get_state = request.POST['cmd_state']
#         get_address = request.POST['address']
#         get_country = request.POST['cmd_country']
#         get_status = request.POST['status']
#         get_location = request.POST['location']
#         get_account_title = request.POST['account_title']
#         get_account_no = request.POST['account_no']
#         get_ibn_number = request.POST['ibn_number']
#         get_branch_code = request.POST['branch_code']
#         get_activation_date = request.POST['activation_date']
#         get_block_date = request.POST['block_date']
#         get_description = request.POST['description']
#         coa_description = ''
#         if get_account_no != "":
#             coa_description = get_branch_code + ',' + get_account_no
#
#         child_update = ChartAccountChild.objects.get(child_code=business_bank.child_code_id)
#         child_update.child_name = get_account_title,
#         child_update.description = coa_description,
#         child_update.save()
#
#         business_bank.account_title = get_account_title
#         business_bank.account_no = get_account_no
#         business_bank.branch_code = get_branch_code
#         business_bank.address = get_address
#         business_bank.city = get_city
#         business_bank.state = get_state
#         business_bank.country = get_country
#         business_bank.activation_date = get_activation_date
#         business_bank.block_date = get_block_date
#         business_bank.ibn_number = get_ibn_number
#         business_bank.description = get_description
#         business_bank.status = get_status
#         business_bank.loc_store_code_id = get_location
#         business_bank.save()
#
#         business_bank = BusinessAccount.objects.get(busi_acc_code=get_busi_code)
#
#     location_store = LocationStore.objects.all()
#
#     param = {
#         'location_store': location_store,
#         'business_bank': business_bank,
#     }
#     return render(request, template_name, param)
#
#
# @login_required(login_url='LoginView')
# def UpdateLocationStoreView(request, code):
#     message = ""
#     get_loc_code = code
#     template_name = "Segments/Location/UpdateLocationStore.html"
#     form = FormLocationStore()
#
#     if request.method == "POST":
#
#         get_company = request.POST['cmd_company']
#         get_Line_business = request.POST['cmd_lob']
#         get_business_sector = request.POST['cmd_bs']
#         # get_cost_center = request.POST['cmd_center']
#         get_location_data = request.POST['cmd_location_data']
#         get_location_city = request.POST['cmd_location_city']
#         loaction_store_inst = LocationStore.objects.get(loc_store_code=get_loc_code)
#         get_form_location = FormLocationStore(request.POST, request.FILES, instance=loaction_store_inst)
#         get_form_inst = get_form_location.save(commit=False)
#
#         FetchLocationStore = LocationStore.objects.filter(loc_code_id=get_location_data)
#         LenFetchLocationStore = len(FetchLocationStore)
#
#         if LenFetchLocationStore == 0:
#             loc_first_code = '{0:03}'.format(1)  # 001
#             combine_code = get_location_data + get_location_city + loc_first_code
#         else:
#             Fetch_latest_record = FetchLocationStore.latest('loc_store_code')
#             get_latest_code = Fetch_latest_record.loc_store_code
#
#             if get_loc_code == get_latest_code:
#
#                 split_latest_record = get_latest_code.split("^")
#                 letter = [x for x in split_latest_record[0]]
#                 remove_letters = letter[3:]
#                 join_split = ''.join(remove_letters)
#                 combine_code = get_location_data + get_location_city + str(join_split)
#             else:
#                 split_latest_record = get_latest_code.split("^")
#                 letter = [x for x in split_latest_record[0]]
#                 remove_letters = letter[3:]
#                 join_split = ''.join(remove_letters)
#                 increment = int(join_split) + 1
#                 format_increment = '{0:03}'.format(increment)
#                 combine_code = get_location_data + get_location_city + str(format_increment)
#
#         get_form_inst.loc_store_code = combine_code
#         get_form_inst.company_code_id = get_company
#         get_form_inst.line_buss_code_id = get_Line_business
#         get_form_inst.buss_sect_code_id = get_business_sector
#         get_form_inst.loc_code_id = get_location_data
#         get_form_inst.city_code_id = get_location_city
#         get_form_inst.status = "Active"
#         get_form_inst.updated_at = datetime.datetime.now()
#         get_form_inst.updated_by = request.session['username']
#         get_form_inst.save()
#         message = "Success"
#     else:
#         form = FormLocationStore()
#         message = "Error"
#
#     Company_list = Company.objects.all().order_by('company_name')
#     lob_list = LineBusiness.objects.all().order_by('line_bus_name')
#     bs_list = BusinessSector.objects.all().order_by('bus_sect_name')
#     center_list = CostCenter.objects.all().order_by('cost_center_name')
#     loc_data_list = LocationData.objects.all().order_by('loc_name')
#     loc_city_list = LocationCity.objects.all().order_by('city_name')
#
#     location_list = list(LocationStore.objects.filter(loc_store_code=get_loc_code).order_by('loc_store_name'))[0]
#
#     params = {'form': form,
#               'message': message,
#               'location_list': location_list,
#               'Company_list': Company_list,
#               'lob_list': lob_list,
#               'bs_list': bs_list,
#               'center_list': center_list,
#               'loc_data_list': loc_data_list,
#               'loc_city_list': loc_city_list
#               }
#
#     return render(request, template_name, params)
#
#
# # SEGMENT VIEW END
#
#
# # GEO HIERARCHY VIEW START
# @login_required(login_url='LoginView')
# def CountryDataView(request):
#     template_name = "GeoHierarchy/CountryData.html"
#     dateTime = datetime.datetime.now()
#     if request.method == 'POST':
#         # GET COUNTRY JSON FILE
#         data = open('static/das/assets/GeoHierarchy/Country.json').read()
#         read_json = json.loads(data)
#         # INSERT INTO TABLE
#         for i in range(len(read_json)):
#             country_name = read_json[i]['country']
#             mobile_code = read_json[i]['code']
#             counttry_code = read_json[i]['iso']
#             InstCounterData = CountryData(
#                 country_code=counttry_code,
#                 country_name=country_name,
#                 country_mobile_code=mobile_code,
#                 status='Active',
#                 created_at=dateTime,
#                 created_by=request.session['username'],
#             )
#             InstCounterData.save()
#     country_data = CountryData.objects.all().order_by('country_name')
#     param = {
#         'country_data': country_data
#     }
#     return render(request, template_name, param)
#
#
# def AddNewCountryView(request):
#     dateTime = datetime.datetime.now()
#     get_country = request.POST['cmd_country']
#     split_get_country = get_country.split('^')
#
#     InstCounterData = CountryData(
#         country_code=split_get_country[0],
#         country_mobile_code=split_get_country[1],
#         country_name=split_get_country[2],
#         status='Active',
#         created_at=dateTime,
#         created_by=request.session['username'],
#     )
#     InstCounterData.save()
#
#     message = "Success"
#     params = {
#         'message': message
#     }
#     return HttpResponse(json.dumps(params))
#
#
# def GetAllCountryView(request):
#     country_data = list(CountryData.objects.all().values('country_code', 'country_name', 'id'))
#     params = {
#         'cmd_list': country_data
#     }
#     return HttpResponse(json.dumps(params))
#
#
# def GetAllCountryFromJsonView(request):
#     data = open('static/das/assets/GeoHierarchy/Country.json').read()
#     read_json = json.loads(data)
#     params = {
#         'cmd_list': read_json
#     }
#     return HttpResponse(json.dumps(params))
#
#
# @login_required(login_url='LoginView')
# def StateDataView(request):
#     template_name = "GeoHierarchy/StateData.html"
#     cursor = connections['default'].cursor()
#
#     query_state_data = "SELECT state_name, state_code, country_code, country_name FROM tbl_country_data ct INNER JOIN tbl_state_data st ON ct.country_code = st.country_code_id"
#     cursor.execute(query_state_data)
#     state_data = DictinctFetchAll(cursor)
#     param = {
#         'state_data': state_data
#     }
#     return render(request, template_name, param)
#
#
# def AddNewStateView(request):
#     dateTime = datetime.datetime.now()
#     get_state_name = request.POST['state_name']
#     get_country_code = request.POST['cmd_country']
#
#     state_auto_code = AutoGenerateSingleDigitNumberCodeForModel(StateData, "state_code")
#     format_state_code = state_auto_code.zfill(2)
#
#     InstStaterData = StateData(
#         state_code=format_state_code,
#         state_name=get_state_name,
#         country_code_id=get_country_code,
#         unique_code=get_country_code + '-' + format_state_code,
#         status='Active',
#         created_at=dateTime,
#         created_by=request.session['username'],
#     )
#     InstStaterData.save()
#     message = "Success"
#     params = {
#         'message': message
#     }
#     return HttpResponse(json.dumps(params))
#
#
# @login_required(login_url='LoginView')
# def CityDataView(request):
#     template_name = "GeoHierarchy/CityData.html"
#     cursor = connections['default'].cursor()
#
#     query_city_data = "select city_code, city_name, state_code, state_name , country_name from tbl_city_data  city INNER JOIN tbl_state_data st ON city.state_code_id = st.state_code INNER JOIN tbl_country_data ct ON ct.country_code = st.country_code_id"
#     cursor.execute(query_city_data)
#     city_data = DictinctFetchAll(cursor)
#     param = {
#         'city_data': city_data
#     }
#     return render(request, template_name, param)
#
#
# def AddNewCityView(request):
#     dateTime = datetime.datetime.now()
#     get_city_name = request.POST['city_name']
#     get_state = request.POST['cmd_state']
#
#     city_auto_code = AutoGenerateSingleDigitNumberCodeForModel(CityData, "city_code").zfill(2)
#     get_state_unique_code = StateData.objects.get(state_code=get_state).unique_code
#
#     InstCityData = CityData(
#         city_code=city_auto_code,
#         city_name=get_city_name,
#         state_code_id=get_state,
#         unique_code=get_state_unique_code + '-' + city_auto_code,
#         status='Active',
#         created_at=dateTime,
#         created_by=request.session['username'],
#     )
#     InstCityData.save()
#     message = "Success"
#
#     params = {
#         'message': message
#     }
#     return HttpResponse(json.dumps(params))
#
#
# @login_required(login_url='LoginView')
# def AreaTownView(request):
#     template_name = "GeoHierarchy/AreaTown.html"
#     cursor = connections['default'].cursor()
#
#     query_area_data = "select country_name, state_name, city_name, area_name from tbl_country_data country INNER JOIN tbl_state_data stat ON country.country_code = stat.country_code_id INNER JOIN tbl_city_data city ON city.state_code_id = stat.state_code INNER JOIN tbl_area_town_data area ON area.city_code_id = city.city_code"
#     cursor.execute(query_area_data)
#     area_data = DictinctFetchAll(cursor)
#     param = {
#         'area_data': area_data
#     }
#     return render(request, template_name, param)
#
#
# def AddNewAreaView(request):
#     dateTime = datetime.datetime.now()
#     get_area_name = request.POST['area_name']
#     get_city = request.POST['cmd_city']
#
#     area_auto_code = AutoGenerateSingleDigitNumberCodeForModel(AreaTownData, "area_code").zfill(4)
#     get_city_unique_code = CityData.objects.get(city_code=get_city).unique_code
#
#     InstAreaTown = AreaTownData(
#         area_code=area_auto_code,
#         area_name=get_area_name,
#         city_code_id=get_city,
#         unique_code=get_city_unique_code + '-' + area_auto_code,
#         status='Active',
#         created_at=dateTime,
#         created_by=request.session['username'],
#     )
#     InstAreaTown.save()
#     message = "Success"
#     params = {
#         'message': message
#     }
#     return HttpResponse(json.dumps(params))
#
#
# # GEO HIERARCHY VIEW END
#
#
# # THIS FUNCTION USED GLOBALLY IN ALL APPLICATION

@login_required(login_url='LoginView')
def FillCmdListByModelView(request):
    table_name = request.POST['table_name']
    column_name = request.POST['column_name']
    column_code = request.POST['column_code']
    model_name = next((m for m in apps.get_models() if m._meta.db_table == table_name), None)

    cmd_list = list(model_name.objects.values(column_code, column_name).order_by(column_name))
    params = {'cmd_list': cmd_list}

    return HttpResponse(json.dumps(params, default=date_handler))


@login_required(login_url='LoginView')
def FillCmdListByModelWithCodeView(request):
    table_name = request.POST['table_name']
    condition_column = request.POST['condition_column']
    condition_split = condition_column.split("=")
    condition_key = condition_split[0]
    condition_value = condition_split[1]

    cmd_column = request.POST['cmd_column']
    column_split = cmd_column.split("^^")
    column_code = column_split[0]
    column_name = column_split[1]

    model_name = next((m for m in apps.get_models() if m._meta.db_table == table_name), None)

    # variable_column = 'name'
    # search_type = 'contains'
    # filter = variable_column + '__' + search_type
    # info = members.filter(**{filter: search_string})

    filter = condition_key
    cmd_list = list(
        model_name.objects.filter(**{filter: condition_value}).values(column_code, column_name).order_by(column_name))
    params = {'cmd_list': cmd_list}

    return HttpResponse(json.dumps(params, default=date_handler))


# PURCHASE PANEL (AJAX)
# MATERIAL LIST

# def MaterialItemInfomationView(request):
#     get_cmd_material = request.POST['cmd_material']
#     material_list = list(MaterialData.objects.filter(material_code=get_cmd_material).values())[0]
#     return HttpResponse(json.dumps({'cmd_list': material_list}, default=date_handler))





# def PurchaseInvoiceWithMaterialView(request):
#     message = ""
#     get_material_code = request.POST['material_code']
#     cursor = connections['default'].cursor()
#
#     # # ORDER ITEMS DETAILS
#     query_foodItem = "WITH pur AS (SELECT material_code_id, uom_code_id, (SUM(delivery_qty)-SUM(sell_qty)) AS quantity FROM tbl_good_receipt_note_item grni INNER JOIN tbl_good_receipt_note grn ON grn.grn_code = grni.grn_code_id WHERE sell_status = 'Pending' AND material_code_id = '" + get_material_code + "' GROUP BY material_code_id, uom_code_id ORDER BY material_code_id) SELECT mt.image, category_name, material_name, mt.uom_code_id, uom_name, quantity, uom_rate FROM pur LEFT OUTER JOIN (SELECT category_name, material_code, material_name, uom_code_id, uom_rate, image FROM tbl_material_data md INNER JOIN tbl_material_category mc ON md.category_code_id = mc.category_code) mt ON pur.material_code_id = mt.material_code LEFT OUTER JOIN tbl_unit_measurement um ON pur.uom_code_id=um.uom_code "
#     cursor.execute(query_foodItem)
#     data_list = DictinctFetchAll(cursor)
#
#     message = "Success"
#
#     return HttpResponse(json.dumps({'data_list': data_list}))
