from django.contrib import admin

# Core: Importing Models
from .models import Item, Order

admin.site.register(Item)
admin.site.register(Order)