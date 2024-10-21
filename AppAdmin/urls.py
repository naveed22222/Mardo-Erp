from django.urls import re_path
from AppAdmin.views import *

urlpatterns = [
    #
    re_path(r'Dashboard/', DashboardView, name='Dashboard'),
    #
    # # ADMIN SETTING
    # re_path(r'^PaymentMethod/', PaymentMethodView, name='PaymentMethod'),
    # re_path(r'^Banklist/', BankListView, name='BankList'),
    #
    # # SEGMENT URLS
    # re_path(r'^Segments/Company', CompanyView, name='CompanyDetail'),
    # re_path(r'^Segments/AddCompany', AddCompanyView, name='AddCompany'),
    # re_path(r'^Segments/Edit-Company/(?P<code>.+)/', UpdateCompanyView, name='UpdateCompany'),
    # re_path(r'^Segments/LineBusiness', LineBusinessView, name='LineBusiness'),
    # re_path(r'^Segments/Busines-Sector', BusinessSectorView, name='BusinessSector'),
    # re_path(r'^Segments/Cost-Center', CostCenterView, name='CostCenter'),
    # re_path(r'^Segments/Natutal-Account', NaturalAccountView, name='NaturalAccount'),
    # re_path(r'^Segments/Location/Details', LocationDataView, name='LocationData'),
    # re_path(r'^Segments/Location/City', LocationCityView, name='LocationCity'),
    # re_path(r'^Segments/Location/Store-Lists', LocationStoreView, name='LocationStore'),
    # re_path(r'^Segments/Location/Store-Create', AddLocationStoreView, name='AddLocationStore'),
    # re_path(r'^Segments/Location/Store-Update/(?P<code>.+)/', UpdateLocationStoreView, name='UpdateLocationStore'),
    # re_path(r'^BusinessBank/', BusinessBankView, name='BusinessBank'),
    # re_path(r'^AddBusinessBank/', AddBusinessBankView, name='AddBusinessBank'),
    # re_path(r'^UpdateBusinessBank/(?P<code>.+)/', UpdateBusinessBankView, name='UpdateBusinessBank'),
    #
    # # GEO HIRARCHY URLS
    # re_path(r'^GeoHirarchy/CountryData', CountryDataView, name='CountryData'),
    # re_path(r'^GeoHirarchy/StateData', StateDataView, name='StateData'),
    # re_path(r'^GeoHirarchy/CityData', CityDataView, name='CityData'),
    # re_path(r'^GeoHirarchy/AreaTown', AreaTownView, name='AreaTown'),
    # # GEO HIRARCHY AJAX URLS
    # re_path(r'^GeoHirarchy/Add_new_country_data', AddNewCountryView, name='AddNewCountry'),
    # re_path(r'^GeoHirarchy/GetAllCountryFromJson', GetAllCountryFromJsonView, name='GetAllCountryFromJson'),
    # re_path(r'^GeoHirarchy/GetAllCountry', GetAllCountryView, name='GetAllCountry'),
    # re_path(r'^GeoHirarchy/Add_new_state_data', AddNewStateView, name='AddNewState'),
    # re_path(r'^GeoHirarchy/Add_new_city_data', AddNewCityView, name='AddNewCity'),
    # re_path(r'^GeoHirarchy/Add_new_area_town', AddNewAreaView, name='AddNewArea'),
    # # AJAX FUNCTION
    # re_path(r'add_line_bussiess', AddLineBusinessView, name='AddLineBusiness'),
    # re_path(r'DeleteLineBussiness', DeleteLineBussiness, name='DeleteLineBussiness'),
    # re_path(r'addbusinesssector', AddBusinessSectorView, name='AddBusinessSector'),
    # re_path(r'DeleteBussinessSector', DeleteBussinessSector, name='DeleteBussinessSector'),
    # re_path(r'add_cost_center', AddCostCenterView, name='AddCostCenter'),
    # re_path(r'add_location_data', AddLocationDataView, name='AddLocationData'),
    # re_path(r'add_location_city', AddLocationCityView, name='AddLocationCity'),
    # re_path(r'unique_location_store_code', LocationStoreCombineCodeView, name='LocationStoreCombineCode'),
    # # re_path(r'DeleteLineBussiness', DeleteLineBussiness, name='DeleteLineBussiness'),
    # # re_path(r'DeleteBussinessSector', DeleteBussinessSector, name='DeleteBussinessSector'),
    # # re_path(r'DeleteCompany', DeleteCompanyView, name='DeleteCompany'),
    # # re_path(r'fetch_product_variety_lists/', FetchProductVarietyLists, name='FetchProductVarietyLists'),
    # # re_path(r'cmd_product_group/', ProductGroupListView, name='ProductroupList'),
    # # re_path(r'cmd_oroduct_variety/', CmdVarietyListView, name='CmdVarietyList'),
    # # re_path(r'cmd_expenditure_category/', CmdCategoryListView, name='CmdCategoryList'),
    # # re_path(r'cmd_expenditure_Subcategory/', CmdSubcategoryListView, name='CmdSubcategoryList'),
    # # re_path(r'single_product_variety_with_code/', FetchFoodVarietyWithProdVariety, name='FetchFoodVarietyWithProdVariety'),
    #
    # # GLOBAL AJAX FUNCTION
    re_path(r'cmd_list_model', FillCmdListByModelView, name='FillCmdListByModel'),
    re_path(r'fill_cmd_model_with_code', FillCmdListByModelWithCodeView, name='FillCmdListByModelWithCode'),
    # re_path(r'add_payment_method', AddPaymentMethodView, name='AddPaymentMethod'),
    # re_path(r'delete_payment_method', DeletePaymentMethodView, name='DeletePaymentMethod'),
    # re_path(r'add_new_bank_list', AddNewBankview, name='AddNewBank'),
    # re_path(r'delete_bank_list', DeleteBankView, name='DeleteBank'),
    #
    # # FOR PAYMENT METHOD
    # re_path(r'cmd_employee_payment_method/', FillCmdEmployeePaymentMethodView, name='FillCmdEmployeePaymentMethod'),
    re_path(r'cmd_payment_method/', FillCmdPaymentMethodView, name='FillCmdPaymentMethod'),
    #
    # # MATERIAL MODEL
    # re_path(r'material_item_information_list/', MaterialItemInfomationView, name='MaterialItemInfomation'),
    #
    # re_path(r'attendance', attendanceView, name='attendance'),
    #
    # re_path(r'purchase_invoice_with_material/', PurchaseInvoiceWithMaterialView, name='PurchaseInvoiceWithMaterial'),



]
