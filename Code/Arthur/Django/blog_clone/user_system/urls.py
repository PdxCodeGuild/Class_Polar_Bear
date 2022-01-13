from django.urls import path
from . import views
'''Create the following views:
Register /register/
form for creating a new user
redirect to /profile/ after registering
Login /login/
form for logging a user in
redirect to /profile/ after logging in
Profile /profile/
a protected page only logged in users can see
just show a welcome message for now'''

# app_name ='user_system'
urlpatterns =[
    path('register/',views.register, name ='register'),
    path('login/',views.user_login, name ='login'),
    path('profile/',views.profile, name='profile'),
    path('logout/',views.user_logout, name = 'logout'),
    

]

