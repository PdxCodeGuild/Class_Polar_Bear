from django.urls import path
from . import views


url_patterns = [
    path(Lab01_Bio.html, views.bio, name='Bio')
]