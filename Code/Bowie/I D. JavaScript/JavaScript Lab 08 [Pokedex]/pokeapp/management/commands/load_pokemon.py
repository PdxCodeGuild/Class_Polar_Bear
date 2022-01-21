import json
from django.core.management.base import BaseCommand

from pokeproj.settings import BASE_DIR
from pokeapp.models import Pokemon

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()

        with open(f"{BASE_DIR}/pokeapp/fixtures/pokemon.json") as f:
            pokemons_list = json.loads(f.read())["pokemon"]
            for pokemon in pokemons_list:
                pokemon["types"] = ",".join(pokemon["types"])
                pokemon["height"] = pokemon["height"] / 10
                pokemon["weight"] = pokemon["weight"] / 10
                pokemon.pop("url")

            Pokemon.objects.bulk_create([Pokemon(**data) for data in pokemons_list])