from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    # path('profile/', views.profile, name='profile'),
    path('add_post/', views.add_post, name='add_post')
]