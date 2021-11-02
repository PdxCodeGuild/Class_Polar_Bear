from django.urls import path
from . import views

app_name = 'grading'
urlpatterns = [
    path('grading/', views.grading, name='grading')
]