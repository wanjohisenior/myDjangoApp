from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, "accounts/login.html", {"form": form, "msg": msg})





def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def dashboard(request):
    return render(request, 'dashboard.html')


import tempfile

from datetime import datetime
from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.conf import settings
from .forms import CreateTenantForm, CreateBuildingForm, CreateLandlordForm, CreateHouseForm, CreateTransactionForm, \
    CreateWaterMeterForm, CreateElectricityMeterForm
from .models import Tenant, Building, Transaction, House, WaterMeter, ElectricityMeter, Landlord
from easy_pdf.views import PDFTemplateView
from .utils import render_to_pdf


class CreateTenantView(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    """
    Class Based View  
    """
    model = Tenant
    fields = '__all__'
    form_class = CreateTenantForm
    initial = {'key': 'value'}
    template_name = 'dbops/tenant_form.html'
    permission_required = "dbops.tenant.Can add tenant"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tenant_list/')

        return render(request, self.template_name, {'form': form})


@login_required(login_url="/login/")
def tenant_list(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    all_tenants = Tenant.objects.all()
    return render(request, 'dbops/tenants.html', {'all_tenants': all_tenants})


class TenantUpdateView(LoginRequiredMixin, UpdateView):
    model = Tenant
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/tenant_list/'


class TenantDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Tenant
    permission_required = "dbops.tenant.Can delete tenant"
    success_url = '/tenant_list/'


class CreateBuildingView(LoginRequiredMixin, CreateView):
    model = Building
    fields = '__all__'
    form_class = CreateBuildingForm
    initial = {'key': 'value'}
    template_name = 'dbops/building_form.html'
    #permission_required = "dbops.tenant.Can add tenant"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/building_list/')

        return render(request, self.template_name, {'form': form})


@login_required(login_url="/login/")
def building_list(request):
    all_buildings = Building.objects.all()
    return render(request, 'dbops/buildings.html', {'all_buildings': all_buildings})


class BuildingUpdateView(LoginRequiredMixin, UpdateView):
    model = Building
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/building_list/'


class BuildingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Building

    permission_required = "dbops.tenant.Can delete building"
    success_url = '/building_list/'


class CreateLandlordView(CreateView):
    model = Landlord
    fields = '__all__'
    form_class = CreateLandlordForm
    initial = {'key': 'value'}
    template_name = 'dbops/landlord_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/landlord_list/')

        return render(request, self.template_name, {'form': form})


@login_required(login_url="/login/")
def landlord_list(request):
    all_landlords = Landlord.objects.all()
    return render(request, 'dbops/landlords.html', {'all_landlords': all_landlords})


class LandlordUpdateView(LoginRequiredMixin, UpdateView):
    model = Landlord
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/landlord_list/'


class LandlordDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Landlord
    permission_required = "dbops.tenant.Can delete landlord"
    success_url = '/landlord_list/'


class CreateTransactionView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = '__all__'
    form_class = CreateTransactionForm
    initial = {'key': 'value'}
    template_name = 'dbops/transaction_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/transaction_list/')

        return render(request, self.template_name, {'form': form})


@login_required(login_url="/login/")
def transaction_list(request):
    all_transactions = Transaction.objects.all()
    return render(request, 'dbops/transactions.html', {'all_transactions': all_transactions})


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/transaction_list/'


class TransactionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Transaction
    success_url = '/transaction_list/'


class CreateHouseView(LoginRequiredMixin, CreateView):
    model = House
    fields = '__all__'
    form_class = CreateHouseForm
    initial = {'key': 'value'}
    template_name = 'dbops/house_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/house_list/')

        return render(request, self.template_name, {'form': form})


@login_required(login_url="/login/")
def house_list(request):
    all_houses = House.objects.all()
    return render(request, 'dbops/houses.html', {'all_houses': all_houses})


class HouseUpdateView(LoginRequiredMixin, UpdateView):
    model = House
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/house_list/'


class HouseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = House
    success_url = '/transaction_list/'


class CreateWaterMeterView(LoginRequiredMixin, CreateView):
    model = WaterMeter
    fields = '__all__'
    form_class = CreateWaterMeterForm
    initial = {'key': 'value'}
    template_name = 'dbops/watermeter_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/watermeter_list/')

        return render(request, self.template_name, {'form': form})


@login_required(login_url="/login/")
def watermeter_list(request):
    all_watermeters = WaterMeter.objects.all()
    return render(request, 'dbops/watermeters.html', {'all_watermeters': all_watermeters})


class WaterMeterUpdateView(LoginRequiredMixin, UpdateView):
    model = WaterMeter
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/watermeter_list/'


class WaterMeterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = WaterMeter
    success_url = '/house_list/'


class CreateElectricityMeterView(LoginRequiredMixin, CreateView):
    model = ElectricityMeter
    fields = '__all__'
    form_class = CreateElectricityMeterForm
    initial = {'key': 'value'}
    template_name = 'dbops/electricitymeter_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/electricitymeter_list/')

        return render(request, self.template_name, {'form': form})


@login_required(login_url="/login/")
def electricitymeter_list(request):
    all_electricitymeters = ElectricityMeter.objects.all()
    return render(request, 'dbops/electricitymeters.html', {'all_electricitymeters': all_electricitymeters})


class ElectricityMeterUpdateView(LoginRequiredMixin, UpdateView):
    model = ElectricityMeter
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/electricitymeter_list/'


class ElectricityMeterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ElectricityMeter
    success_url = '/electricitymeter_list/'


from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import get_template


class GeneratePDF(View):

    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        all_landlords = Landlord.objects.all()
        context = {
            'all_landlords': all_landlords
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            qs = all_landlords.filter(surname='sample')
            filename = "Invoice_%s.pdf" %qs
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def RevenueReportPDF(request):
    return render(request, 'pdf/revenue_report.html',)

    """""""""
class RevenueReportPDF(View):
    template = get_template('pdf/revenue_report.html')



    def get(self, request, *args, **kwargs):
        template = get_template('pdf/revenue_report.html')
        all_transactions = Transaction.objects.all()
        context = {
            'all_transactions': all_transactions
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/revenue_report.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            qs = all_transactions.filter(transationtype='transationtype')
            filename = "Revenue_report%s.pdf" % qs
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
        
    """""""""""
