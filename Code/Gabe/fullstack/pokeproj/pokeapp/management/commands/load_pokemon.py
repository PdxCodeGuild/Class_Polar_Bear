from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('hello')
        with open('pokemon.txt', encoding='utf-8') as pokemon_json:
            # for pokemon in pokemon_json['pokemon']:
            #     print(pokemon.height)
            self.stdout.write('Nice')
            contents = pokemon_json.read()
            print(contents)