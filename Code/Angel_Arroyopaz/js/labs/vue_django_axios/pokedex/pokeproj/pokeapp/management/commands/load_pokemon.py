from django.core.management.base import BaseCommand
import json
from pokeapp.models import Pokemon

class Command(BaseCommand):

    def handle(self, *args, **options):
        # write the code here
        with open('pokeapp\management\commands\pokemon.json', 'r') as file:
            contents = file.read()
        
        data = json.loads(contents)
        pokemon = Pokemon()
        pokemon_delete = Pokemon.objects.all()
        pokemon_delete.delete()

        for i in data['pokemon']:
            pokemon.pk = None
            if i['height'] < 11:
                i['height'] *= 0.1
            if i['weight'] < 11:
                i['weight'] *= 0.1
            if i['height'] > 10:
                i['height'] -= 10
            if i['weight'] > 10:
                i['weight'] -= 10
    
            new_types = ','.join(i['types'])
            pokemon.number = i['number']
            pokemon.name = i['name']
            pokemon.height = i['height']
            pokemon.weight = i['weight']
            pokemon.image_front = i['image_front']
            pokemon.image_back = i['image_back']
            pokemon.types = new_types
            pokemon.save()
        

        