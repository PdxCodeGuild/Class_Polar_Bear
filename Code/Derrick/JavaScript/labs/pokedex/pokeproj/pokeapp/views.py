from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon
import json

# Create your views here.

def home_page(request):
    return render(request,'pokeapp/index.html')

def get_pokemon(request):
    with open('pokemon.json') as file:
        plain_text = file.read()
        json_text = json.loads(plain_text)

    all_pokemon = json_text
    pokedex = all_pokemon['pokemon']

    for pokemon in pokedex:
        poke = Pokemon()
        poke.number = pokemon['number']
        poke.name = pokemon['name']
        poke.height = pokemon['height']
        poke.weight = pokemon['weight']
        poke.image_front = pokemon['image_front']
        poke.image_back = pokemon['image_back']
        poke.types = pokemon['types']
        poke.save()
        

    return JsonResponse({'pokemon': pokedex})

    

