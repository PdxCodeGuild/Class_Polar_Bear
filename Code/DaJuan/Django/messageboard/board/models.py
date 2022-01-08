from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Message(models.Model):
    text_content = models.CharField(max_length=240)
    user = models.CharField(max_length=40)
    date = models.DateField(auto_created=True)

    def __str__(self):
        return f'{self.date}--{self.text_content},{self.user}'