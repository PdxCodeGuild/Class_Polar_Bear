from django.urls import path
from . import views

urlpatterns = [
path('', views.routing, name='routing'),
path('<int:num>', views.number, name = 'num'),
path('bf_bio', views.bf_bio, name='bf_bio'),
path('blog', views.blog, name='blog'),
path('reeces_pizza', views.reeces_pizza, name='reeces_pizza'),
path('buttons', views.buttons, name='buttons')
]