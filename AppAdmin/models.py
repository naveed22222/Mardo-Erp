from django.db import models
# from AppChartAccount.models import *


# Create your models here.

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_code = models.CharField(max_length=200, null=True, unique=True)  # 01
    company_name = models.TextField(max_length=100, null=True)  # Mardo Group
    uan_no = models.TextField(max_length=200, null=True)
    ntn_no = models.TextField(max_length=200, null=True)
    strn_no = models.TextField(max_length=200, null=True)
    address = models.TextField(max_length=200, null=True)
    mobile = models.TextField(max_length=200, null=True)
    area = models.TextField(max_length=100, null=True)
    city = models.TextField(max_length=200, null=True)
    state = models.TextField(max_length=200)
    image = models.ImageField(upload_to='Company', default="")
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_company'

    def __str__(self):
        return self.company_name


class LineBusiness(models.Model):
    id = models.AutoField(primary_key=True)
    line_bus_code = models.CharField(max_length=100, null=True, unique=True)  # 01
    line_bus_name = models.TextField(max_length=100, null=True)  # Restaurant, Cafe, Factory, Construction
    status = models.TextField(max_length=100, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "tbl_line_business"

    def __str__(self):
        return self.line_bus_name


class BusinessSector(models.Model):
    id = models.AutoField(primary_key=True)
    bus_sect_code = models.CharField(max_length=100, null=True, unique=True)  # 01
    bus_sect_name = models.TextField(max_length=100, null=True)  # Retail, Corporate, Online, Splasing
    status = models.TextField(max_length=100, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "tbl_business_sector"

    def __str__(self):
        return self.bus_sect_name


class CostCenter(models.Model):
    id = models.AutoField(primary_key=True)
    cost_center_code = models.CharField(max_length=200, null=True, unique=True)
    cost_center_name = models.TextField(max_length=100,
                                        null=True)  # Retail, Marketing, Human Resource, Admin, Procurement, Accounts & Finance, Information Technology    status = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=100, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_cost_center'

    def __str__(self):
        return self.cost_center_name


class LocationData(models.Model):
    id = models.AutoField(primary_key=True)
    loc_code = models.CharField(max_length=200, null=True, unique=True)
    loc_name = models.TextField(max_length=100, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_location_data'

    def __str__(self):
        return self.loc_name


class LocationCity(models.Model):
    id = models.AutoField(primary_key=True)
    city_code = models.CharField(max_length=200, null=True, unique=True)
    city_name = models.TextField(max_length=100, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_location_city'

    def __str__(self):
        return self.city_name


class LocationStore(models.Model):
    id = models.AutoField(primary_key=True)
    loc_store_code = models.CharField(max_length=200, null=True, unique=True)
    loc_store_name = models.TextField(max_length=100, null=True)
    company_code = models.ForeignKey(Company, to_field='company_code', on_delete=models.CASCADE, null=True)
    line_bus_code = models.ForeignKey(LineBusiness, to_field='line_bus_code', on_delete=models.CASCADE, null=True)
    bus_sect_code = models.ForeignKey(BusinessSector, to_field='bus_sect_code', on_delete=models.CASCADE, null=True)
    cost_center_code = models.ForeignKey(CostCenter, to_field='cost_center_code', on_delete=models.CASCADE, null=True)
    loc_code = models.ForeignKey(LocationData, to_field='loc_code', on_delete=models.CASCADE, null=True)
    city_code = models.ForeignKey(LocationCity, to_field='city_code', on_delete=models.CASCADE, null=True)
    mobile = models.TextField(max_length=200, null=True)
    address = models.TextField(max_length=200, null=True)
    area = models.TextField(max_length=100, null=True)
    image = models.ImageField(upload_to='LocationStore', default="")
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_location_store'

    def __str__(self):
        return self.loc_store_name


class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    pm_code = models.CharField(max_length=200, null=True, unique=True)  # PM-1
    pm_name = models.TextField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_payment_method'

    def __str__(self):
        return self.pm_name


class BankData(models.Model):
    id = models.AutoField(primary_key=True)
    bank_name = models.TextField(max_length=200, null=True)
    bank_code = models.CharField(max_length=200, null=True, unique=True)  # BANK CODE BASE
    description = models.TextField(max_length=200, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_bank_data'

    def __str__(self):
        return self.bank_name


class JournalVoucher(models.Model):
    id = models.AutoField(primary_key=True)
    bpv_code = models.CharField(max_length=200, null=True, unique=True)  # BPV-1
    description = models.TextField(max_length=200, null=True)
    debit = models.IntegerField(null=True)
    credit = models.IntegerField(null=True)
    join_code = models.CharField(max_length=100, null=True)  # e.g PUR-1. EMP-1
    join_name = models.TextField(max_length=100, null=True)  # e.g Purchase Code, Employee Code
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_journal_voucher'

    def __str__(self):
        return self.id


# CRM MODEL STARTS
class CountryData(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.TextField(max_length=200, null=True)
    country_code = models.CharField(max_length=200, null=True, unique=True)
    country_mobile_code = models.CharField(max_length=200, null=True)
    country_name = models.TextField(max_length=200, null=True)
    image = models.ImageField(upload_to='Country', default="")
    description = models.TextField(max_length=300, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_country_data'

    def __str__(self):
        return self.id


class StateData(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.TextField(max_length=200, null=True)
    state_code = models.CharField(max_length=200, null=True, unique=True)
    unique_code = models.CharField(max_length=200, null=True)
    country_code = models.ForeignKey(CountryData, to_field='country_code', on_delete=models.CASCADE, null=True)
    state_name = models.TextField(max_length=200, null=True)
    image = models.ImageField(upload_to='State', default="")
    description = models.TextField(max_length=300, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_state_data'

    def __str__(self):
        return self.id


class CityData(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.TextField(max_length=200, null=True)
    city_code = models.CharField(max_length=200, null=True, unique=True)
    unique_code = models.CharField(max_length=200, null=True)
    state_code = models.ForeignKey(StateData, to_field='state_code', on_delete=models.CASCADE, null=True)
    city_name = models.TextField(max_length=200, null=True)
    image = models.ImageField(upload_to='City', default="")
    description = models.TextField(max_length=300, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_city_data'

    def __str__(self):
        return self.id


class AreaTownData(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.TextField(max_length=200, null=True)
    area_code = models.CharField(max_length=200, null=True, unique=True)
    unique_code = models.CharField(max_length=200, null=True)
    city_code = models.ForeignKey(CityData, to_field='city_code', on_delete=models.CASCADE, null=True)
    area_name = models.TextField(max_length=200, null=True)
    image = models.ImageField(upload_to='Area', default="")
    description = models.TextField(max_length=300, null=True)
    status = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_area_town_data'

    def __str__(self):
        return self.id
# CRM MODEL END


class BusinessAccount(models.Model):
    id = models.AutoField(primary_key=True)
    busi_acc_code = models.CharField(max_length=200, null=True, unique=True)
    account_title = models.CharField(max_length=200, null=True)
    account_no = models.TextField(max_length=200, null=True)
    branch_code = models.IntegerField(null=True)
    address = models.TextField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    activation_date = models.DateField(null=True)
    block_date = models.DateField(null=True)
    ibn_number = models.TextField(max_length=200, null=True)
    description = models.TextField(max_length=300, null=True)
    status = models.TextField(max_length=200, null=True)
    loc_store_code = models.ForeignKey(LocationStore, to_field='loc_store_code', on_delete=models.CASCADE, null=True)

    # child_code = models.ForeignKey(ChartAccountChild, to_field='child_code', on_delete=models.CASCADE,
    #                                null=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'tbl_business_account'

    def __str__(self):
        return self.id
