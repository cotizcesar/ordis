from django.contrib import admin

# Core: Importing Models
from .models import Connection, Post, Comment

admin.site.register(Connection)
admin.site.register(Post)
admin.site.register(Comment)