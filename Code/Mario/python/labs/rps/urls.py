from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('/<str:choice>', views.selected, name='selected')
]
