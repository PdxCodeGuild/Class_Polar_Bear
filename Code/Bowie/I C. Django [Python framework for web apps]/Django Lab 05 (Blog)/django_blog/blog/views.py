from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from blog.models import BlogPost
from blog.forms import BlogPostForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "register.html", {"form": form})
    form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                form.add_error("Wrong username or password")
                return render(request, "login.html", {"form": form})
        else:
            return render(request, "login.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="/login")
def profile_view(request):
    user_posts = BlogPost.objects.filter(user=request.user)
    return render(request, "profile.html", {"posts": [post.title for post in user_posts]})

@login_required(login_url="/login")
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("profile")
        else:
            return render(request, "create_post.html", {"form": form})
    form = BlogPostForm()
    return render(request, "create_post.html", {"form": form})