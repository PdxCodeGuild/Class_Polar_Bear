from django.db import models

# Create your models here.

class GroceryItem(models.Model):
    description = models.TextField(max_length=255)
    completed = models.BooleanField(default=False)