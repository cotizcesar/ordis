from django.shortcuts import render

from django.db.models import Q

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Codex: Importing Models
from .models import Quest, QuestWalkthrough, Item, ItemAttribute, ItemAttributeValue, ItemAbilityValue

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
        context['latest_companions'] = Item.objects.filter(tipe=2).values('name', 'image', 'slug', 'description', 'release_date').order_by('-release_date')[:3]
        context['latest_warframes'] = Item.objects.filter(tipe=1).values('name', 'image', 'slug', 'description', 'release_date').order_by('-release_date')[:3]
        context['latest_weapons'] = Item.objects.filter(tipe=3).values('name', 'slug', 'image', 'tipe', 'description').order_by('-date_created')[:3]
        return context

class Companions(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Companions, self).get_context_data(**kwargs)
        context['companions'] = Item.objects.filter(Q(tipe=4) | Q(tipe=2)).values('name', 'image', 'slug', 'release_date').order_by('name')
        return context

class Weapons(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Weapons, self).get_context_data(**kwargs)
        context['weapons'] = Item.objects.filter(tipe=3).values('name', 'image', 'slug', 'release_date').order_by('name')
        return context

class Warframes(TemplateView):
    template_name = 'codex/codex.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Warframes, self).get_context_data(**kwargs)
        context['warframes'] = Item.objects.filter(tipe=1).values('name', 'image', 'slug', 'release_date').order_by('name')
        return context

class ItemDetail(DetailView):
    model = Item
    template_name = 'codex/detail/codex_universe_item_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['attributes'] = ItemAttributeValue.objects.filter(item=self.object.id).select_related()
        context['abilities'] = ItemAbilityValue.objects.filter(item=self.object.id).select_related()[:4]
        context['pasive'] = ItemAbilityValue.objects.filter(item=self.object.id).select_related()[4:5]
        return context