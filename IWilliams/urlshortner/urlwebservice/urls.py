from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saveurl', views.saveurl, name='saveurl'),
    path('<str:code>', views.urlredirect, name='urlredirect' )
]

