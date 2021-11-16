from django.contrib.auth.models import User
from django.db import models

class Comment(Post):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

class Post(models.Model):
    text = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=1)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.text[:21]} {self.published_date.year}, {self.published_date.month}, {self.published_date.day}. {self.published_date.hour}:{self.published_date.minute}"

