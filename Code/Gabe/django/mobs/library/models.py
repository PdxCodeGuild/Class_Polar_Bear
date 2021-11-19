from django.db import models


# Create your models here.
class Author(models.Model):
    author = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'{self.author}'


class Status(models.Model):
    user = models.CharField(max_length=40)
    checkout = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.checkout}, {self.timestamp}'


class Book(models.Model):
    title = models.CharField(max_length=80)
    publish_date = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}, {self.author}, {self.publish_date}, {self.status.checkout}'
