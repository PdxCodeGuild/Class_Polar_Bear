from django.shortcuts import render 
import datetime

# Create your views here.
def birthday(request):
    now = datetime.datetime.now()
    theday = now.day
    themonth = now.month
    birthday = False
    if theday == 25 and themonth == 10:
        birthday = True

    return render(request, 'birthday/index.html',{'birthday': birthday})