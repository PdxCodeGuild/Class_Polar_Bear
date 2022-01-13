from django.urls import path
from .import views

urlpatterns = [
    #routing
    path('routing',views.routing, name ='routing'),

]