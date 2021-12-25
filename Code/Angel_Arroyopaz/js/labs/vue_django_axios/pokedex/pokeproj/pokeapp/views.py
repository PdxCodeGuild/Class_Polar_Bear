from django.shortcuts import render
from django.http import JsonResponse

from .models import Pokemon

# Create your views here.
def index(request):
    return render(request, 'pokeapp/index.html')

def pokemons(request):
    pokemons = Pokemon.objects.all().order_by('number')
    data = []
    for pokemon in pokemons:
        data.append({
            'number': pokemon.number,
            'name': pokemon.name,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'image_front': pokemon.image_front,
            'image_back': pokemon.image_back,
            'types': pokemon.types,
        })

    return JsonResponse({'pokemons': data})