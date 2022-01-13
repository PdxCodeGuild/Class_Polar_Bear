from django.urls import path
from . import views

app_name = 'valuechain'
urlpatterns = [
    path('manufacturing/', views.manufacturing, name='manufacturing'),
    path('save_supplier/', views.save_supplier, name='save_supplier'),
    path('save_manufacturer/', views.save_manufacturer, name='save_manufacturer'),
    path('save_customer/', views.save_customer, name='save_customer'),
]