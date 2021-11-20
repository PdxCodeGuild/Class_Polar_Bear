from django.db import models

# Create your models here.

# Author
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

# Logentry
class State(models.Model):
    user = models.CharField(max_length=40)
    checked_out = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} checked out a book.'

# Book
class Book(models.Model):
    title = models.CharField(max_length=80)
    published_date = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    state = models.OneToOneField(State, on_delete=models.PROTECT)

    def __str__(self) -> str:
        if self.state.checked_out:
            return f'{self.title} has been checked out by {self.state.user}.'
        else:
            return f'{self.title} is available.'
