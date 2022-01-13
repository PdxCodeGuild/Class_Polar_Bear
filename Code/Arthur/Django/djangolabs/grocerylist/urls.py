from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name ='grocerylist'
urlpatterns =[
       path('',views.index, name ='index'),
       path('add_grocery',views.add_grocery, name ='add'),
       path('check/<int:item_id>/',views.check_grocery, name ='check')
]