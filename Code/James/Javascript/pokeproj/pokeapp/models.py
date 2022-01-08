from django.db import models

# Create your models here.

class Pokemon(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    height = models.FloatField(default=3)
    weight = models.FloatField(default=50)
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.CharField(max_length=200)

    def __str__(self):
        return self.number, self.name, self.height, self.weight, self.image_front, self.image_back, self.types