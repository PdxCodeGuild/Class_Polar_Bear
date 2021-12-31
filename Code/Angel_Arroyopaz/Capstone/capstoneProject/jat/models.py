from django.db import models
from django.db import models

# Create your models here.
class NewApplication(models.Model):
    job_title = models.CharField(max_length=20)
    notes = models.TextField()
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.job_title