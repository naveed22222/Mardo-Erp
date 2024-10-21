from django import forms
from AppAdmin.models import *

STATUS_ARRAY = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)


class FormCompany(forms.ModelForm):
    company_code = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Company Code'}))
    company_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Company Name'}))
    uan_no = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Uan Number'}))
    ntn_no = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Ntn Number'}))
    strn_no = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Strn Number'}))
    address = forms.CharField(max_length=100, required=False, widget=forms.Textarea(
        attrs={"rows": 3, "cols": 20, 'class': 'form-control', 'placeholder': 'Enter Your Address'}))
    mobile = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}))
    area = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Area'}))
    city = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter City name'}))
    state = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter State Name'}))
    status = forms.CharField(max_length=50, required=False, widget=forms.Select(
        choices=STATUS_ARRAY, attrs={'class': 'form-control select2'}))
    image = forms.FileField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'accept': 'image/png, image/jpeg, image/gif'}))

    class Meta:
        model = Company
        fields = [
            'company_code',
            'company_name',
            'uan_no',
            'ntn_no',
            'strn_no',
            'address',
            'mobile',
            'area',
            'city',
            'state',
            'status',
            'image',
        ]


class FormLocationStore(forms.ModelForm):
    loc_store_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Store Name'}))
    address = forms.CharField(max_length=100, required=False, widget=forms.Textarea(
        attrs={"rows": 3, "cols": 20, 'class': 'form-control', 'placeholder': 'Enter Your Address'}))
    mobile = forms.CharField(max_length=100, required=False, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}))
    area = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Area'}))
    image = forms.FileField(required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'accept': 'image/png, image/jpeg, image/gif'}))

    class Meta:
        model = LocationStore
        fields = [
            'loc_store_name',
            'address',
            'mobile',
            'area',
            'image',
        ]
