from django.contrib import admin

# Core: Importing Models
from .models import Item

admin.site.register(Item)