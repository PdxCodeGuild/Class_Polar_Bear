from django.urls import path
from . import views

urlpatterns = [
    path('Bio/', views.Bio, name='Bio Lab'),
    path('Blog/', views.Blog, name='Blog'),
    path('Company/', views.Company, name='Company'),
    path('Animations/', views.Animations, name='Animations')
]