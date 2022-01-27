from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.title

