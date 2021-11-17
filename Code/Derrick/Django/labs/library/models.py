from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Author(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first} {self.last}'

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=CASCADE)
    checked_out = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title} by {self.author}'