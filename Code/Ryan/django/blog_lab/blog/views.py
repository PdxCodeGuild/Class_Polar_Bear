from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# how to ensure server does not post verbose error messages
from django.shortcuts import get_object_or_404

# how to ensure user is logged in before doing something
from django.contrib.auth.decorators import login_required

from .models import Blurb, Reply
from .forms import NewBlurbForm, NewReplyForm
# Create your views here.

# Home page for displaying most recent messages
def index(request):
    blurbs = Blurb.objects.all().order_by('-published_date')[:20]
    
    return render(request, 'blurbs/index.html', {
        'blurbs': blurbs,
        'form': NewBlurbForm()
    })

# prevents anonymous users from doing this stuff protects on server side
@login_required
def new_blurb(request):
    if request.method == "POST":
        # takes data from POST and fills out the form
        form = NewBlurbForm(request.POST)
        if form.is_valid():
            blurb = Blurb()
            blurb.user = request.user
            blurb.text = form.cleaned_data['text']
            blurb.save()
    return HttpResponseRedirect(reverse('index'))

@login_required
def delete_blurb(request, blurb_id):

    #  will check if exists first, then handle blurb
    if Blurb.objects.filter(id=blurb_id, user=request.user).exists():
        blurb = Blurb.objects.get(id=blurb_id, user=request.user)
        blurb.delete()
    
    return HttpResponseRedirect(reverse('index'))

@login_required
def like(request, blurb_id):
    if Blurb.objects.filter(id=blurb_id).exists():
        blurb = Blurb.objects.get(id=blurb_id)
        blurb.likes += 1
        blurb.save()
    return HttpResponseRedirect(reverse('index'))

@login_required
def dislike(request, blurb_id):
    if Blurb.objects.filter(id=blurb_id).exists():
        blurb = Blurb.objects.get(id=blurb_id)
        blurb.dislikes += 1
        blurb.save()
    return HttpResponseRedirect(reverse('index'))


def detail(request, blurb_id):
    blurb = Blurb.objects.get(id=blurb_id)
    form = NewReplyForm()
    return render(request, 'blurbs/detail.html', {
        'blurb': blurb,
        'form': form
    })

def reply(request, blurb_id):
    blurb = Blurb.objects.get(id=blurb_id)
    form = NewReplyForm(request.POST)
    if form.is_valid():
        reply = Reply()
        reply.user = request.user
        reply.text = form.cleaned_data['text']
        reply.save()
    # if Blurb.objects.filter(id=blurb_id).exists():
        # if request.method == "POST":
            # blurb = Blurb.objects.get(id=blurb_id)
            # blurb.reply = Reply(request.POST)
            # blurb.save()
    # return render(request, 'blurbs/detail.html', {
    #     'blurb': blurb,
    #     'reply': reply
    # })
    return HttpResponseRedirect(reverse('detail', kwargs={
        'blurb': blurb
    }))
# def new_blurb(request):
#     if request.method == "POST":
#         # takes data from POST and fills out the form
#         form = NewBlurbForm(request.POST)
#         if form.is_valid():
#             blurb = Blurb()
#             blurb.user = request.user
#             blurb.text = form.cleaned_data['text']
#             blurb.save()
#     return HttpResponseRedirect(reverse('index'))

    # return HttpResponseRedirect(reverse('index'))