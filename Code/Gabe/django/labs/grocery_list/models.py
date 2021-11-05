import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class GroceryItem(models.Model):
    item_text = models.CharField(max_length=100)
    is_complete = models.BooleanField(auto_created=True, default=False)
    deleted = models.BooleanField(auto_created=True, default=False)
    date_added = models.DateTimeField('date & time', auto_created=True)

    def __str__(self) -> str:
        return f'Item: {self.item_text}, Date Added: {self.date_added}, Completed? {self.is_complete}'
