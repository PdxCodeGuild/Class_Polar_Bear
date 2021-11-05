from django.db import models

class PollQuestion(models.Model):

    question = models.CharField('question', max_length=100)

    def __str__(self):
        return self.question

class PollChoice(models.Model):

    choice = models.CharField('choice', max_length=100)
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

