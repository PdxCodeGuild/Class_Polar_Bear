from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost
# Create your views here.

def get_posts(request):
    posts = BlogPost.objects.all()
    data = []
    for post in posts:
        data.append({
            'id' : post.id,
            'title': post.title,
            'body': post.body,
            'created_date' : post.created_date
        })

    return JsonResponse({'posts' : data})