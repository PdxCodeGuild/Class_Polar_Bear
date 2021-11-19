from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.publish_date} {self.author}'

    def checked_out(self):
        tracks = Track.objects.filter(book=self.id)
        print(tracks)
        if len(tracks) > 0:
            tracks = list(tracks)
            # reverse tracks
            # return tracks[0].checkout
            return tracks[-1].checkout
        else:
            return False

class Track(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    checkout = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book} {self.user} {self.checkout} {self.timestamp}'



