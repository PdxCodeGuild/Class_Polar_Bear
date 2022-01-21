from django.shortcuts import render

def bio(request):
    return render(request, "routing/bio.html")