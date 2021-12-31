from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        with open('pokeapp\management\commands\pokemon.json', 'r') as f:
            contents = json.load(f)
            print(contents['pokemon'][0]['name'])
            # Pokemon.all().delete()
            for i in contents['pokemon']:
                pokemon = Pokemon()
                pokemon.number = i['number']
                pokemon.name = i['name']
                pokemon.height = i['height']
                pokemon.weight = i['weight']
                pokemon.image_front = i['image_front']
                pokemon.image_back = i['image_back']
                pokemon.types = i['types']
                pokemon.save()
                print(pokemon)
