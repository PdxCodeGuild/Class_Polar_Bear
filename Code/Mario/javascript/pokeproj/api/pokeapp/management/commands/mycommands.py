from django.core.management.base import BaseCommand


class Command(BaseCommand):
    print('hello')

    def handle(self, *args, **options):
        print('hello')
        with open('pokemon.json', 'r') as f:
            contents = f.read()
            print(contents)
