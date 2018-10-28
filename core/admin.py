from django.contrib import admin

# Core: Importing Models
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)