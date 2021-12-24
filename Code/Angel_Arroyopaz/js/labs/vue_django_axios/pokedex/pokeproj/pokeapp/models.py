from django.db import models

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=30)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=30)
    image_back = models.CharField(max_length=30)
    types = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.number} - {self.name}'