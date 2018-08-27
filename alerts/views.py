from django.shortcuts import render

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

class Alerts(TemplateView):
    template_name = 'alerts.html'