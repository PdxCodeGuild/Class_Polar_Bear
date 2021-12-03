from django.db import models

class GroceryItem(models.Model):
    item = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.item} - {self.status}'