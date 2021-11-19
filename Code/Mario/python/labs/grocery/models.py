from django.db import models


class GroceryItem(models.Model):
    desc = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
