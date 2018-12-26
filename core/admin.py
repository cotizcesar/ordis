from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Core: Importing Models
from .models import UserProfile, Connection, Post, Comment

class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    pass

class ConnectionResource(resources.ModelResource):
    class Meta:
        model = Connection

@admin.register(Connection)
class ConnectionAdmin(ImportExportModelAdmin):
    pass

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    pass

class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    pass
