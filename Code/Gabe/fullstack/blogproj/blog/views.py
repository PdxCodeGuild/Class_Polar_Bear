from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def get_posts(request):
    posts = BlogPost.objects.all().order_by('-created_date')
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'created_date': post.created_date.strftime('%m %d %Y %H:%M:%S')
        })

    return JsonResponse({'posts': data})
