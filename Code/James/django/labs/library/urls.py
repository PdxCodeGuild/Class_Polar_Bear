from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('checkin/', views.checkin, name='checkin'),
    path('checkout/<int:book_id>/', views.checkout, name='checkout'),
]