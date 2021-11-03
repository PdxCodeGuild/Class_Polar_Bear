from django.urls import path
from . import views

urlpatterns = [
    path('bio/', views.request_bio),
    path('blog/', views.request_blog),
    path('company/', views.request_company),
    path('animations/', views.request_animations)
]