from django.db import models

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=25)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=25)
    image_back = models.CharField(max_length=25)
    types = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.number}, {self.name}, {self.height}, {self.weight}, {self.image_front}, {self.image_back},{self.types}'