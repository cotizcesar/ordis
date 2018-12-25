from django import forms

# Django: Importing User Model
from django.contrib.auth.models import User

# Models
from .models import UserProfile, Post, Comment

class SignupForm(forms.ModelForm):
    model = User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        help_texts = {
            'first_name': 'If you want to use your first name you can place it here.',
            'last_name': 'If you use your first name, you should also put your last name, so its easier to know what your name really is.',
            'username': 'Use the IGN to validate your registration.',
            'email': 'Use your personal email, preferably one that is not associated with Warframe.',
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar', 'bio')
        help_texts = {
            'avatar': 'Only images in JPG and PNG are allowed.',
            'bio': 'Use this space for text, you have a limit of 140 characters.',
        }

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
        help_texts = {
            'text': 'Use this space for text, you have a limit of 280 characters.',
        }
