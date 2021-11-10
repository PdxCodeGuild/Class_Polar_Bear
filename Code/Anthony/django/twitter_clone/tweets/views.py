from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Tweet
from .forms import NewTweetForm

# Home page for displaying most recent messages
def index(request):
    tweets = Tweet.objects.all().order_by('-published_date')[:20]
    return render(request, 'tweets/index.html', {
        'tweets': tweets,
        'form': NewTweetForm()
    })

@login_required
def new_tweet(request):
    if request.method == "POST":
        form = NewTweetForm(request.POST)
        if form.is_valid():
            tweet = Tweet()
            tweet.user = request.user
            tweet.text = form.cleaned_data['text']
            tweet.save()

    return HttpResponseRedirect(reverse('index'))

@login_required
def delete_tweet(request, tweet_id):
    # Option 1, will fail if tweet does not exist
    # tweet = Tweet.objects.get(id=tweet_id, user=request.user)

    # Option 2, Display 404 page if tweet does not exist
    # tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)

    # Option 3, check if exists first, then handle tweet.
    if Tweet.objects.filter(id=tweet_id, user=request.user).exists():
        tweet = Tweet.objects.get(id=tweet_id, user=request.user)
        tweet.delete()
    return HttpResponseRedirect(reverse('index'))
