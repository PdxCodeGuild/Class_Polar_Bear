from django.db import models

class Pkmn(models.Model):
    hght = models.IntegerField((""))
    name = models.CharField((""), max_length=30)
    nmbr = models.IntegerField((""))
    wght = models.FloatField((""))

    def __str__(self):
        return self.name

