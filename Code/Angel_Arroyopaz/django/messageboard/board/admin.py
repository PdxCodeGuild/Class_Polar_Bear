from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Message) # Message being the model we created in models.py


















# create super user in terminal using: python3 manage.py createsuperuser
# and follow the prompts

# go to localhost:8000/admin to log in
