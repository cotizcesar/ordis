from django.shortcuts import render

# Django: Importing User Model
from django.contrib.auth.models import User

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Market: Importing Models
from .models import Item, Order

class Market(TemplateView):
    template_name = 'market.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Market, self).get_context_data(**kwargs)
        context['wts'] = Order.objects.all().filter(want='S').exclude(is_active=False)
        context['wtb'] = Order.objects.all().filter(want='B').exclude(is_active=False)
        return context

class ItemDetail(DetailView):
    model = Item
    template_name = "item_detail.html"
    pk_url_kwarg = "item_id"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_context_data(self, *args, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['wts'] = Order.objects.all().filter(item=self.get_object(), want='S').exclude(is_active=False)
        context['wtb'] = Order.objects.all().filter(item=self.get_object(), want='B').exclude(is_active=False)
        context['childs'] = Item.objects.filter(parent=self.get_object())
        return context