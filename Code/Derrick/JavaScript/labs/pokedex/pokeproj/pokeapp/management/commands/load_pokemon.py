from django.core.management.base import BaseCommand
import requests, json

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        data = {'pokemon':[]}
        num_pokemon = 152
        for i in range(1, num_pokemon):
            # get the data from the pokemon api
            response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(i))
            pokeapi_data = json.loads(response.text)

            # extract the relevant portions of data
            number = pokeapi_data['id']
            name = pokeapi_data['name']
            height = pokeapi_data['height'] / 10
            weight = pokeapi_data['weight'] / 10
            image_front = pokeapi_data['sprites']['front_default']
            image_back = pokeapi_data['sprites']['back_default']
            url = 'https://pokemon.fandom.com/wiki/' + name
            types = [type['type']['name'] for type in pokeapi_data['types']]

            # put the relevant data into a dictionary
            pokemon = {
                'number': number,
                'name': name,
                'height': height,
                'weight': weight,
                'image_front': image_front,
                'image_back': image_back,
                'types': types,
                'url': url
            }

            # add the pokemon to our list
            data['pokemon'].append(pokemon)
            # give the user some feedback
            with open('pokemon.json', 'w') as file:
                file.truncate(0)
                new_data = json.dumps(data)
                file.write(new_data)