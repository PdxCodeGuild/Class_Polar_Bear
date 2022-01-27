from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

def index(request):
    question_list = Question.objects.order_by('pub_date')
    context = {"question_list": question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choices = question.choice_set.filter(pk__in=request.POST.getlist("choice"))
    if not selected_choices:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    
    for choice in selected_choices:
        choice.votes += 1
        choice.save()
    
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))