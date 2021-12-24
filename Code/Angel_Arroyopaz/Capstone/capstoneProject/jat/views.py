from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import NewApplication
import json

# Create your views here.
def home_page(request):
    return render(request, 'jat/index.html')

def dashboard_page(request):
    return render(request, 'jat/dashboard.html')

def get_posts(request):
    posts = NewApplication.objects.all()
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'job_title': post.job_title,
            'notes': post.notes,
            'status': post.status
        })

    return JsonResponse({'posts': data})