from django.db import models

# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=240)
    user = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text} by {self.user} -- {self.date}'