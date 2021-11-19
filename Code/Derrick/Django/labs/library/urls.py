from django.urls import path 
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('checkin/',views.checkin_page,name='checkin_page'),
    path('checkin/<int:book_id>',views.checkin_book,name='checkin_book'),
    path('checkout/',views.checkout_page,name='checkout_page'),
    path('checkout/<int:book_id>',views.checkout_book,name='checkout_book')
]