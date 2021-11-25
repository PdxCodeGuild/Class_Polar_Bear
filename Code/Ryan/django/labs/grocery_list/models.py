from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    item = models.CharField(max_length=40)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item} -- {self.completed}'