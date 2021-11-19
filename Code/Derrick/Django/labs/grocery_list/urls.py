from django.urls import path 
from . import views

urlpatterns = [
    path('',views.render_grocery_list,name='grocery_list'),
    path('update/',views.update_list,name='update_list'),
    path('remove/<int:g_id>',views.remove_item,name='remove_item'),
    path('mark_completed/<int:g_id>',views.mark_completed,name='mark_completed')
]