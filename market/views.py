from django.shortcuts import render

# Django: Importing User Model
from django.contrib.auth.models import User

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

class Market(TemplateView):
    template_name = 'market.html'