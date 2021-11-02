from django.urls import path

from . import views

urlpatterns = [
    path('messageboard/', views.home_page, name="home_page"),
    path('new_message/', views.new_message, name="new_message")
]