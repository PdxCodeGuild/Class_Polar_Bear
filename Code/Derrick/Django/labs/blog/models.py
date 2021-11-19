from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=25)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    public = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.body[:10]}, {self.user}, {self.public}, {self.date_created}'
