from django.http import HttpResponse, JsonResponse
from .models import Pokemon
from django.shortcuts import render

'''
Create a view pokemon that gets a list of Pokemon out of the database 
and turns them into a dictionary to be passed to JsonResponse. 
Verify this works by going to localhost:8000/pokemon/ 
in your browser and seeing a list of pokemon in JSON.'''

def pokemon(request):
    '''context = {
        'message': 'Hello World!'
    }
    return render(request, 'pokeapp/index.html', context)'''
    pokemon = Pokemon.objects.all()
    pokelist = []
    for critter in pokemon:
        pokelist.append({
            'number': critter.number,
            'name': critter.name,
            'height': critter.height,
            'weight': critter.weight,
            'image_front': critter.image_front,
            'image_back': critter.image_back,
            'types': critter.types,
        })
    return JsonResponse({'pokemon': pokelist})

'''Create a second view index that renders a template containing a Vue app 
(don't forget to change the delimiters on the Vue app so it doesn't conflict 
with the template rendering syntax). Use Axios to send a request to the pokemon 
view and display a list of pokemon on the page with their images. In your Vue app, 
you'll need to switch the delimiters so they don't conflict with the Django template rendering syntax.'''

def index(request):
    return render(request, 'pokeapp/index.html')