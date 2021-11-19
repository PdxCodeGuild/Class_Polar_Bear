from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    # max_length is a required parameter for CharField
    code = models.CharField(max_length=6)
    url = models.URLField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.code} -- {self.url} -- {self.counter}'