from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=80)
    publish_date = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.title}, {self.author}, {self.publish_date}, {self.status.checkout}'
