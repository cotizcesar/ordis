from django import forms

# Django: Importing User Model
from django.contrib.auth.models import User

# Models
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image', 'video')