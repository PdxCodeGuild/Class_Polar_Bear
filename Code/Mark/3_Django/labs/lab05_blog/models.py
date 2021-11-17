from django.contrib.auth.models import User
from django.db import models

class Comment(Post):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

class Post(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=4000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    public = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}: {self.body[:21]}, {self.date_created}"

