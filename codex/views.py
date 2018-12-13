from django.shortcuts import render

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Codex: Importing Models
from .models import Quest, QuestWalkthrough, Weapon, Stat, Warframe, WarframeAbility

class Codex(TemplateView):
    template_name = 'codex/codex.html'

class Quests(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Quests, self).get_context_data(**kwargs)
        context['quests'] = Quest.objects.all().values('name', 'image', 'slug').order_by('quest_order')
        return context

class QuestDetail(DetailView):
    model = Quest
    template_name = 'codex/detail/codex_quest_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super(QuestDetail, self).get_context_data(**kwargs)
        context['walkthroughs'] = QuestWalkthrough.objects.filter(quest=self.get_object()).order_by('pk')
        return context

class Universe(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Universe, self).get_context_data(**kwargs)
        context['latest_warframes'] = Warframe.objects.all().values('name', 'image', 'slug', 'description', 'release_date').order_by('-release_date')[:3]
        context['latest_weapons'] = Weapon.objects.all().values('name', 'slug', 'image', 'tipe', 'description').order_by('-date_created')[:3]
        return context

class Weapons(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Weapons, self).get_context_data(**kwargs)
        context['weapons'] = Weapon.objects.all().values('name', 'image', 'slug').order_by('name')
        return context

class WeaponsPrimary(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WeaponsPrimary, self).get_context_data(**kwargs)
        context['weapons'] = Weapon.objects.filter(tipe='P').values('name', 'image', 'slug').order_by('name')
        return context

class WeaponsSecondary(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WeaponsSecondary, self).get_context_data(**kwargs)
        context['weapons'] = Weapon.objects.filter(tipe='S').values('name', 'image', 'slug').order_by('name')
        return context

class WeaponsMelee(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WeaponsMelee, self).get_context_data(**kwargs)
        context['weapons'] = Weapon.objects.filter(tipe='M').values('name', 'image', 'slug').order_by('name')
        return context

class WeaponDetail(DetailView):
    model = Weapon
    template_name = 'codex/detail/codex_universe_weapon_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super(WeaponDetail, self).get_context_data(**kwargs)
        context['stats'] = Stat.objects.filter(weapon=self.get_object())
        return context

class Warframes(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Warframes, self).get_context_data(**kwargs)
        context['warframes'] = Warframe.objects.all().values('name', 'image', 'slug').order_by('name')
        return context

class WarframeDetail(DetailView):
    model = Warframe
    template_name = 'codex/detail/codex_universe_warframe_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super(WarframeDetail, self).get_context_data(**kwargs)
        context['abilities'] = WarframeAbility.objects.filter(warframe=self.get_object())
        return context