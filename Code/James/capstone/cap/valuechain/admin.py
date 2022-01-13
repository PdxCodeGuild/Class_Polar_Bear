from django.contrib import admin
from .models import Supplier
from .models import Manufacturer
from .models import Customer

admin.site.register(Supplier)
admin.site.register(Manufacturer)
admin.site.register(Customer)