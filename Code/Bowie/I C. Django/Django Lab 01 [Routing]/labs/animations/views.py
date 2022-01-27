from django.shortcuts import render

def animations(request):
    return render(request, "animations/animations.html")