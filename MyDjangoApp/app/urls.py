from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import login_view, register_user, dashboard, CreateTenantView, CreateBuildingView, CreateHouseView, CreateWaterMeterView, CreateTransactionView, \
    CreateLandlordView, CreateElectricityMeterView, TenantUpdateView, TenantDeleteView, BuildingUpdateView, \
    BuildingDeleteView, HouseUpdateView, TransactionUpdateView, TransactionDeleteView, WaterMeterUpdateView, \
    ElectricityMeterUpdateView, LandlordUpdateView, WaterMeterDeleteView, ElectricityMeterDeleteView, \
    LandlordDeleteView, GeneratePDF
    
from . import views


urlpatterns = [
    path('', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('dashboard/', dashboard, name="dashboard"),


        path('create_tenant', CreateTenantView.as_view(), name='create_tenant'),
    path('create_building', CreateBuildingView.as_view(), name='create_building'),
    path('create_house', CreateHouseView.as_view(), name='create_house'),
    path('create_watermeter', CreateWaterMeterView.as_view(), name='create_watermeter'),
    path('create_transaction', CreateTransactionView.as_view(), name='create_transaction'),
    path('create_landlord', CreateLandlordView.as_view(), name='create_landlord'),
    path('create_electricitymeter', CreateElectricityMeterView.as_view(), name='create_electricitymeter'),

    path('tenant_list/', views.tenant_list, name='tenant_list'),
    path('building_list/', views.building_list, name='building_list'),
    path('house_list/', views.house_list, name='house_list'),
    path('transaction_list/', views.transaction_list, name='transaction_list'),
    path('watermeter_list/', views.watermeter_list, name='watermeter_list'),
    path('electricitymeter_list/', views.electricitymeter_list, name='electricitymeter_list'),
    path('landlord_list/', views.landlord_list, name='landlord_list'),

    path('edit_tenant/<int:pk>/', TenantUpdateView.as_view(), name='edit_tenant'),
    path('edit_building/<int:pk>/', BuildingUpdateView.as_view(), name='edit_building'),
    path('edit_house/<int:pk>/', HouseUpdateView.as_view(), name='edit_house'),
    path('edit_transaction/<int:pk>/', TransactionUpdateView.as_view(), name='edit_transaction'),
    path('edit_watermeter/<int:pk>/', WaterMeterUpdateView.as_view(), name='edit_watermeter'),
    path('edit_electricitymeter/<int:pk>/', ElectricityMeterUpdateView.as_view(), name='edit_electricitymeter'),
    path('edit_landlord/<int:pk>/', LandlordUpdateView.as_view(), name='edit_landlord'),

    path('delete_tenant/<int:pk>/', TenantDeleteView.as_view(), name='delete_tenant'),
    path('delete_building/<int:pk>/', BuildingDeleteView.as_view(), name='delete_building'),
    path('delete_transaction/<int:pk>/', TransactionDeleteView.as_view(), name='delete_transaction'),
    path('delete_watermeter/<int:pk>/', WaterMeterDeleteView.as_view(), name='delete_watermeter'),
    path('delete_electricitymeter/<int:pk>/', ElectricityMeterDeleteView.as_view(), name='delete_electricitymeter'),
    path('delete_landlord/<int:pk>/', LandlordDeleteView.as_view(), name='delete_landlord'),

    path('pdf/', GeneratePDF.as_view(), name='pdf'),
#    path('revenue_report/', RevenueReportPDF.as_view(), name='revenue_report' ),
    path('rev_report/', views.RevenueReportPDF, name='rev_report'),
]
