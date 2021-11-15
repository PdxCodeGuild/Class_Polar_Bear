from django.db.models.query import get_prefetcher
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at the results of question %s ." % question_id) # %s is an old school f string that needed to be in order

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(requestion, question_id):
    return HttpResponse("You're boting on the %s."  % question_id)