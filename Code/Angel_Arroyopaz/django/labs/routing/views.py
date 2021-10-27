from django.shortcuts import render

# Create your views here.
def bio(request):
    return render(request, 'routing/bio.html')


def blog(request):
    return render(request, 'routing/blog.html')

def contact_us(request):
    return render(request, 'routing/contact_us.html')

def company(request):
    return render(request, 'routing/company.html')

def animations(request):
    return render(request, 'routing/animations.html')