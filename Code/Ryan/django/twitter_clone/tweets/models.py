from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=120)
    # related references the user so you can look at user.tweets to get all user tweets
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=1)
    # likes = models.ManyToManyField(User, related_name='liked')
    # dislikes = models.ManyToManyField(User, related_name='disliked')
    # auto_now updates when model changes
    # auto_now_true adds time when model is created
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.text[:21]} {self.published_date.year} / {self.published_date.month} / {self.published_date.day} @ {self.published_date.hour}:{self.published_date.minute}"
    

class Reply(Tweet):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='replies')

