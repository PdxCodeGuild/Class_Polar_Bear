from django.db import models
from django.db.models.fields import CharField, IntegerField, URLField

# Create your models here.
class ShortenedURL(models.Model):
    code = CharField(max_length=15)
    url = URLField(max_length=100)
    counter = IntegerField(default=0)