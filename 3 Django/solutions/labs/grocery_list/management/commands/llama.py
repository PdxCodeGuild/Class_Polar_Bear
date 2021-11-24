from django.core.management.base import BaseCommand
import random
from grocery_list.models import GroceryItem, Department

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        GroceryItem.objects.all().delete()
        departments = list(Department.objects.all())

        with open('./foods.txt') as file:
            text = file.read()

        items = text.split('\n')
        
        for item in items:
            if item:
                grocery_item = GroceryItem()
                grocery_item.item = item
                grocery_item.department = random.choice(departments)
                grocery_item.save()
