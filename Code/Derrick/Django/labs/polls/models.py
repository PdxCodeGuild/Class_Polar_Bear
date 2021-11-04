from django.db import models
from django.db import models 
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    q_text = models.CharField( 'question', max_length=200)
    q_date = models.DateTimeField('date')

    def __str__(self):
        return self.q_text

    def recent(self):
        return self.q_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    c_text = models.CharField('choice', max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.c_text