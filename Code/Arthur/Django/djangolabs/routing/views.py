from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def routing(request):
    return render(request,'routing/Bio.html')
