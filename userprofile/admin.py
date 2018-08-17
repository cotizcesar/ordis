from django.contrib import admin

# Core: Importing Models
from .models import UserProfile

admin.site.register(UserProfile)