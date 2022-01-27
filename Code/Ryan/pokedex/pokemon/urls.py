from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,name='index'),
    path('catchem_all/',views.catchem, name='catchem'),
]