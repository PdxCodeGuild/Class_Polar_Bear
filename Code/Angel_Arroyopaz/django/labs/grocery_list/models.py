from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class GroceryItem(models.Model):
    item = CharField(max_length=200)
    completed = False

    def __str__(self):
        return f'{self.item}'

class Completed(models.Model):
    completed_item = CharField(max_length=200)

    def __str__(self):
        return f'{self.completed_item}'

class Incomplete(models.Model):
    incomplete_item = CharField(max_length=200)

    def __str__(self):
        return f'{self.incomplete_item}'