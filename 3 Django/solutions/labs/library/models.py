from django.db import models

# Create your models here.

# Author
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


# Book
class Book(models.Model):
    title = models.CharField(max_length=80)
    published_date = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.title} -{self.author.last_name}, {self.author.first_name}'
