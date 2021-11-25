from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
# Create your models here.
class Cheep(models.Model):
    chirp = models.CharField(max_length=120)
    date_published = models.DateTimeField(auto_now=True)
    # have a user import from native django CASCADE pushes down through all tied keys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

# how to represent this data as text later
def __str__(self):
    return f"{self.user}: {self.date_published} -- {self.chirp}"