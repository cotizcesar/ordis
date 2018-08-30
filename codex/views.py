from django.shortcuts import render

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Codex: Importing Models
from .models import Quest

class Codex(TemplateView):
    template_name = 'codex.html'

    #def get_context_data(self, *args, **kwargs):
    #    context = super(Codex, self).get_context_data(**kwargs)
    #    context['wts'] = Order.objects.filter(want='S').order_by('-date_created').exclude(is_active=False)[:30]
    #    context['wtb'] = Order.objects.filter(want='B').order_by('-date_created').exclude(is_active=False)[:30]
    #    return context

class Quests(TemplateView):
    template_name = 'codex_quests.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Quests, self).get_context_data(**kwargs)
        context['quests'] = Quest.objects.all().values('name', 'image', 'slug')
        return context