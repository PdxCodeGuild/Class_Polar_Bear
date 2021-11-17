from .forms import NewPostForm
from .models import Post

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    posts = Post.objects.all().order_by('-date_created')[:20]
    return render(request, 'lab05_blog/index.html', {'posts': posts, 'form': NewPostForm()})

@login_required
def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.user = request.user
            post.body = form.cleaned_data['body']
            post.save()
    return HttpResponseRedirect(reverse('index'))

@login_required
def delete_post(request, post_id):
    if Post.objects.filter(id=post_id, user=request.user).exists():
        post = Post.objects.get(id=post_id, user=request.user)
        post.delete()
    return HttpResponseRedirect(reverse('index'))

def detail(request, post_id):
    post = Post.objects.get(id=Post_id)
    return render(request, 'lab05_blog/detail.html', {'post': post})

