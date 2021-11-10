from django.shortcuts import render

from .models import Tweet

# Home page for displaying most recent messages
def index(request):
    tweets = Tweet.objects.all().order_by('-published_date')[:20]
    return render(request, 'tweets/index.html', {
        'tweets': tweets
    })