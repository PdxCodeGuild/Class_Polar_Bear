from multiprocessing import context
from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BlogPost

def profile(request):
    if not request.user.is_anonymous: 
        blog_list = BlogPost.objects.filter(user=request.user)
        args = {
            'blog_list': blog_list
        }
        print(blog_list, 'blog list')
        return render(request, 'users/profile.html', args)
    else:
        print('failure to login')

def add_post(request):
    title = request.POST['title']
    body = request.POST['body']
    blog_post = BlogPost()
    blog_post.title = title
    blog_post.body = body
    blog_post.user = request.user
    blog_post.save()
    blog_list = BlogPost.objects.filter(user=request.user)
    args = {
            'blog_list': blog_list
        }
    return render(request, 'users/profile.html', args)