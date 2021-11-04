from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# Create your views here.

def index(request):
    q = Question.objects.get(id=1)
    q_list = Question.objects.all().order_by('-q_date')[:5]
    return render(request, 'polls/index.html',{'q_list':q_list})
    # return render(request, 'polls/index.html', {})

def details(request, q_id):
    q = get_object_or_404(Question,id=q_id)
    return render(request, 'polls/details.html',{'q': q})

def results(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/results.html', {'q': q})

def vote(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        
        return render(request, 'polls/details.html', {
            'q': q,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))