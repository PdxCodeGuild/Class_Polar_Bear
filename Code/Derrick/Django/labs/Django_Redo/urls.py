from django.urls import path
from . import views 

urlpatterns = [
    path('pw_generator/',views.render_generator, name='pw_generator'),
    path('pw_generator/create',views.create, name='create'),   
]