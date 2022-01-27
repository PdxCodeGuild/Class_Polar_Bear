from django.db import models

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=250)
    image_back = models.CharField(max_length=250)
    types = models.CharField(max_length=100)

    def __str__(self):
        return self.name