from django.db.models import Model, CharField, TextField, ForeignKey, BooleanField, DateTimeField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class BlogPost(Model):
    title = CharField(max_length=255)
    body = TextField()
    user = ForeignKey(to=User, on_delete=CASCADE)
    public = BooleanField(default=True)
    date_created = DateTimeField(auto_now_add=True)
    date_edited = DateTimeField(auto_now=True)
