from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon
import json

'''
Write a custom management command load_pokemon.py to load the data from pokemon.json into your database. 
You can do this by saving the file next to your .py file and using open. 
In the first line of your management command, 
you may want to delete all the records in the table so each time you run it you start with a clean slate. 
To verify that the data was loaded, log into your admin panel and check that the pokemon are there.

The data was taken from the PokeAPI, 
height is in decimeters (divide by 10 to get meters) and weight is in hectograms (divide by 10 to get kilograms). 
You may want to convert these values before saving them.
'''

class Command(BaseCommand):

    def handle(self, *args, **options):
        # write the code here
        # print('hello!')

        # Delete all the records in the table (Done manually through Admin account. How do I do this with Python?)

        # Open the file
        with open('pokeapp\management\commands\pokemon.json', 'r') as f:
            contents = f.read()
        
        # Load the json data
        jsondata = json.loads(contents)

        # Load the Model
        pokedata = Pokemon()

        # Parse the pokedata and add to model. Fix Pokedata reference.
        for i in jsondata['pokedata']:
            pokedata.number = i['number']
            pokedata.name = i['name']
            pokedata.height = i['height']/10
            pokedata.weight = i['weight']/10
            pokedata.image_front = i['image_front']
            pokedata.image_back = i['image_back']
            pokedata.types = i['types']            
            pokedata.save() # Json.loads?

