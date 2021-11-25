from django.core.management.base import BaseCommand

from grocery_list.models import GroceryItem

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./foods.txt') as file:
            text = file.read()
        items = text.split('\n')

        for item in items:
            grocery_item = GroceryItem()
            grocery_item.item = item
            grocery_item.save()


# This command will go through and delete items
# GroceryItem.objects.all().delete()