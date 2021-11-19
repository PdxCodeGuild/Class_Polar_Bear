from django import forms
from django.db import models

class Grocery(models.Model):
    grocery = models.CharField(max_length=200)

    def __str__(self):
        return self.grocery

