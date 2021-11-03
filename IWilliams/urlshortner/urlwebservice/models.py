from django.db import models


# Create your models here.
class ShortenedURL(models.Model): 
    code = models.CharField(max_length = 200)
    url = models.URLField(max_length = 200)
    counter = models.IntegerField(default=0)
