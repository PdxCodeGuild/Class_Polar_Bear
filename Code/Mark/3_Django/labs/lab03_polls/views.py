from . import models
from django.shortcuts import render

def index(request):
    q = models.PollQuestion.objects.get(id=1)
    q_list = models.PollQuestion.objects.all()
    return render(request, 'lab03_polls/index.html', {'q_list':q_list})

def poll_features(request, q_id):
    return render(request, 'lab03_polls/poll_features.html', {'q': q})

def poll_results(request, q_id):
    return render(request, 'lab03_polls/poll_results.html', {'q': q})

def poll_vote(request, q_id):
    selected_choice = q.choice_set.get(pk=request.POST['choice'])

