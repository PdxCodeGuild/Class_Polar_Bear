from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blurb(models.Model):
    text = models.CharField(max_length=500)
    # related references the user so you can look at user.blurb to get all user blurbs
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blurbs')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    # likes = models.ManyToManyField(User, related_name='liked')
    # dislikes = models.ManyToManyField(User, related_name='disliked')
    # auto_now updates when model changes
    # auto_now_true adds time when model is created
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.text[:21]} {self.published_date.year} / {self.published_date.month} / {self.published_date.day} @ {self.published_date.hour}:{self.published_date.minute}"
    

class Reply(Blurb):
    blurb = models.ForeignKey(Blurb, on_delete=models.CASCADE, related_name='replies')
