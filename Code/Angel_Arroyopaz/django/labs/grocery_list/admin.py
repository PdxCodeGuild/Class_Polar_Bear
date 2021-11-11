from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.GroceryItem)
admin.site.register(models.Incomplete)
admin.site.register(models.Completed)