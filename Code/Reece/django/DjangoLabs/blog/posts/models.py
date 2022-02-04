from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogposts')
    public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Blog Post'