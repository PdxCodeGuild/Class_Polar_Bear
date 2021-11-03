from django.urls import path
from . import views

urlpatterns = [
    path('animations/', views.render_animations, name='animations'),
    path('bio/', views.render_bio, name='bio'),
    path('blog/', views.render_blog, name='blog'),
    path('company/', views.render_company, name='company')
]

