from django.shortcuts import render

# Create your views here.
def bio(request):
    return render(request, 'routing/bio.html')

def blog(request):
    return render(request, 'routing/blog.html')

def company(request):
    return render(request, 'routing/company.html')

def animations(request):
    return render(request, 'routing/animations.html')