from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class  blogpost(models.Model):
    title = models.CharField(max_length=120)
    body =models.TextField(max_length=120)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    # public = models.BooleanField(True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=1)
    
#note go to admin.py and register the model here it will appear in the database
    #represent our model as a string and you can add the string as you wish
    def __str__(self):
        return f"{self.title}:{self.user}:{self.body[0:21]}"

        #you can shorted the datea {self.date_created.year},{self.date_created.day},hour minute and day


# # reference user/profile from blog
# blogpost=blogpost()
# print(blogpost.user)

# # reference blog from user using related_name
# user=User()
# print(user.blogpost)