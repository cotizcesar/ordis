from django.shortcuts import render

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Codex: Importing Models
from .models import Quest, Weapon

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
        context['quests'] = Quest.objects.all().values('name', 'image', 'slug').order_by('-date_created')
        return context

class QuestDetail(DetailView):
    model = Quest
    template_name = 'codex_quest_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class Universe(TemplateView):
    template_name = 'codex_universe.html'

class Weapons(TemplateView):
    template_name = 'codex_universe_weapons.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Weapons, self).get_context_data(**kwargs)
        context['weapons'] = Weapon.objects.all().values('name', 'image', 'slug').order_by('name')
        return context

class WeaponsPrimary(TemplateView):
    template_name = 'codex_universe_weapons_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WeaponsPrimary, self).get_context_data(**kwargs)
        context['weapons'] = Weapon.objects.filter(tipe='P').values('name', 'image', 'slug').order_by('name')
        return context

class WeaponsSecondary(TemplateView):
    template_name = 'codex_universe_weapons_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WeaponsSecondary, self).get_context_data(**kwargs)
        context['weapons'] = Weapon.objects.filter(tipe='S').values('name', 'image', 'slug').order_by('name')
        return context

class WeaponsMelee(TemplateView):
    template_name = 'codex_universe_weapons_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WeaponsMelee, self).get_context_data(**kwargs)
        context['weapons'] = Weapon.objects.filter(tipe='M').values('name', 'image', 'slug').order_by('name')
        return context

class WeaponDetail(DetailView):
    model = Weapon
    template_name = 'codex_universe_weapon_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'