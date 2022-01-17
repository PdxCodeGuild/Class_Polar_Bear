from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Pkmn

def pkmn(self):
    return JsonResponse(list(Pkmn.objects.values()), safe=False)

