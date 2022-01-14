from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    item =models.CharField(max_length=120)
    completed = models.BooleanField(default=False)

    #print it nicely in an admin panel
    def __str__ (self):
        return f"{self.item} -- {self.completed}"

