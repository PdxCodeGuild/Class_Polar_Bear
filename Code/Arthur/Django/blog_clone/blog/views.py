from django import forms
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
#the class we just created
from .models import blogpost


from .forms import newBlogForm
# Create your views here
#displaying blogs
def index(reqest):
    #this goes in descending order
    blog = blogpost.objects.all().order_by('-title')[:20]
    return render(reqest,'blog/index.html',{
        'blog':blog,
        'form':newBlogForm()

    })
@login_required
def new_blog(request):
    if request.method == "POST":
        form = newBlogForm(request.POST)
        if form.is_valid():
            blogpos = blogpost()
            blogpos.user=request.user
            blogpos.text = form.cleaned_data['text']
            blogpos.save()

    return HttpResponseRedirect(reverse('index'))
