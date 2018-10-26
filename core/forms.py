from django import forms

# Django: Importing User Model
from django.contrib.auth.models import User

# Models
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image', 'video')
        help_texts = {
            'text': 'Usa este espacio para texto, tienes un limite de 280 caracteres.',
            'image': 'Only images in JPG and PNG are allowed.',
            'video': 'Copy and paste an URL from the following sites: YouTube.com, Twitch.tv, Vimeo.com or Giphy.com.',
        }