from django.db import models
from django.db.models.fields import CharField
# Create your models here.

class ShortenedURL(models.Model):
    code = models.CharField(max_length=6)
    url = models.URLField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.code} -- {self.url} -- {self.counter}'