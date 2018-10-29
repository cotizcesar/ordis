from django import forms

# Django: Importing User Model
from django.contrib.auth.models import User

# Models
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image', 'video')
        help_texts = {
            'text': 'Use this space for text, you have a limit of 280 characters.',
            'image': 'Only images in JPG and PNG are allowed.',
            'video': 'Copy and paste an URL from the following sites: YouTube.com, Twitch.tv, Vimeo.com or Giphy.com.',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)