from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon
import json

# Create your views here.

def index(request):
    return render(request,'pokemon/index.html')

def catchem(request):
    with open('pokemon.json') as file:
        plain_text = file.read()
        json_text = json.loads(plain_text)

    all_pokemon = json_text
    pokemons = all_pokemon['pokemon']

    for pokemon in pokemons:
        creature = Pokemon()
        creature.number = pokemon['number']
        creature.name = pokemon['name']
        creature.height = pokemon['height']
        creature.weight = pokemon['weight']
        creature.image_front = pokemon['image_front']
        creature.image_back = pokemon['image_back']
        creature.types = pokemon['types']
        creature.save()
        
    print(request.body)
    return JsonResponse({'pokemon': pokemons})


    
