from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.forms.widgets import Textarea

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE)
    public = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f'{self.title} \n {self.body[:30]} \n {self.user} - ({self.public}) \n {self.date_created} \n {self.date_edited}'

    def __str__(self):
        return f'{self.title}'