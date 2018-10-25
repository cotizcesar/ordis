from django.contrib import admin

# Core: Importing Models
from .models import Post

admin.site.register(Post)