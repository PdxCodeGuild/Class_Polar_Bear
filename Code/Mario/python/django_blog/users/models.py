from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    body = models.models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_created=True)
    date_Edited = models.DateTimeField(auto_now=True)
