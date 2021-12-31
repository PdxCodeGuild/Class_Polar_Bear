from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon


def pokemon(self):
    return JsonResponse(list(Pokemon.objects.values()), safe=False)
