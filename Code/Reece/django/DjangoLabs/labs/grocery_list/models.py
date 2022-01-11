from django.db import models

# Create your models here.
class Item(models.Model):
    item = models.CharField(max_length=240)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.item
