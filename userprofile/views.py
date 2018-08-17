from django.shortcuts import render

# Django: Importing User Model
from django.contrib.auth.models import User

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

class UserProfileDetailView(DetailView):
    model = User
    template_name = 'userprofile_index.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'