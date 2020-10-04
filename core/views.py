from django.shortcuts import render

#! Django: Generic CBV
from django.views.generic import (
    TemplateView,
    ListView,
    FormView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)


class Index(TemplateView):
    template_name = "index.html"
