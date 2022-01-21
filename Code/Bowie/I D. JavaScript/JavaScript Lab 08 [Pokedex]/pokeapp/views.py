from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse

from .models import Pokemon

def get_pokemon(request):
    name_param = request.GET.get("name", "")
    pokemon_list = [model_to_dict(pokemon) for pokemon in Pokemon.objects.filter(name__icontains=name_param)]
    return JsonResponse({"pokemon_list": pokemon_list})

def index(request):
    return render(request, "pokeapp/index.html")
