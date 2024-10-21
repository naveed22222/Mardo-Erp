from django import forms
from AppEmployee.models import *

GENDER_ARRAY = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

DUTY_TYPE_ARRAY = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

ETHNIC_GROUP_ARRAY = (
    ('Punjabis', 'Punjabis'),
    ('Sindhis', 'Sindhis'),
    ('Pashtuns', 'Pashtuns'),
    ('Other', 'Other'),
)

MATERIAL_STATUS_ARRAY = (
    ('Un-Married', 'Un-Married'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
    ('Other', 'Other'),
)

RATE_TYPE_ARRAY = (
    ('Salary', 'Salary'),
    ('Daily', 'Daily'),
    ('Wages', 'Wages'),
)

PAY_FREQUENCY_ARRAY = (
    ('Monthly', 'Monthly'),
    ('Daily', 'Daily'),
)

STATUS_ARRAY = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)


class FormEmployeeInfo(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'autocomplete':'off', 'class': 'form-control', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'autocomplete':'off', 'class': 'form-control', 'placeholder': 'Enter Last Name'}))
    title = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'autocomplete':'off', 'class': 'form-control', 'readonly': 'true'}))
    gender = forms.CharField(max_length=100, required=False, widget=forms.Select(
        choices=GENDER_ARRAY, attrs={'class': 'form-control form-select select2-no-search select2-hidden-accessible',
                                     'placeholder': 'Enter Gender'}))
    duty_type = forms.CharField(max_length=50, required=False, widget=forms.Select(
        choices=DUTY_TYPE_ARRAY, attrs={'class': 'form-control form-select select2-no-search select2-hidden-accessible',}))
    address = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'autocomplete':'off', 'class': 'form-control', 'placeholder': 'Enter Address'}))
    cnic_no = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'autocomplete':'off', 'class': 'form-control', 'placeholder': 'Enter CNIC NO.'}))

    class Meta:
        model = EmployeeInformation
        fields = [
            'first_name',
            'last_name',
            'title',
            'gender',
            'duty_type',
            'address',
            'cnic_no',

        ]

class FormDeductionFixed(forms.ModelForm):
    deduction_amount = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}))
    description = forms.CharField(max_length=100, required=False, widget=forms.Textarea(
        attrs={"rows": 3, "cols": 20, 'class': 'form-control', 'placeholder': 'Enter Reason for Deduction'}))

    class Meta:
        model = DeductionFixed
        fields = [
            'deduction_amount',
            'description',
        ]


class FormDeductionTrans(forms.ModelForm):
    trans_amount = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}))
    description = forms.CharField(max_length=100, required=False, widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20, 'class': 'form-control', 'placeholder': 'Enter Reason for Deduction'}))

    class Meta:
        model = DeductionTransaction
        fields = [
            'trans_amount',
            'description',
        ]


class FormAllowanceFixed(forms.ModelForm):
    allowance_amount = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}))
    description = forms.CharField(max_length=100, required=False, widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20, 'class': 'form-control', 'placeholder': 'Enter Reason for Allowance'}))

    class Meta:
        model = AllowanceFixed
        fields = [
            'allowance_amount',
            'description',
        ]


class FormAllowanceNonFixed(forms.ModelForm):
    trans_amount = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}))
    description = forms.CharField(max_length=100, required=False, widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20, 'class': 'form-control', 'placeholder': 'Enter Reason for Allowance'}))

    class Meta:
        model = AllowanceTransaction
        fields = [
            'trans_amount',
            'description',
        ]
