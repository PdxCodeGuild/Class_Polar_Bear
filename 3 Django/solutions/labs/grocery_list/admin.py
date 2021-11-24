from django.contrib import admin
from .models import Department, GroceryItem

# Register your models here.
admin.site.register(Department)
admin.site.register(GroceryItem)