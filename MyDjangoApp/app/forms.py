from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ROLES(forms.Form):
    ROLES_TYPES = [
        ('Administrator', 'Administratot'),
        ('Accountant', 'Accountant'),
        ('Secretary', 'Secretary'),
        ('Staff', 'Staff')
    ]
    ROLES_TYPES = forms.CharField(
        widget=forms.RadioSelect(choices=ROLES_TYPES))




from django import forms

from . import models
from .models import Tenant, Building, Landlord, House, Transaction, WaterMeter, ElectricityMeter


class CreateTenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'


class CreateBuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'


class CreateLandlordForm(forms.ModelForm):

    class Meta:
        model = Landlord
        fields = '__all__'


class CreateHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'


class CreateTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


class CreateWaterMeterForm(forms.ModelForm):
    class Meta:
        model = WaterMeter
        fields = '__all__'


class CreateElectricityMeterForm(forms.ModelForm):
    class Meta:
        model = ElectricityMeter
        fields = '__all__'