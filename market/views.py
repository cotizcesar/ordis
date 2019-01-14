from django.shortcuts import render

# Django: Internal Library
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

# Codex: Importing Models
from codex.models import Item

# Market: Importing Models
from .models import Order

# Market: Importing Forms
from .forms import OrderForm, OrderFormBeast

class Market(TemplateView):
    template_name = 'market/market.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(Market, self).get_context_data(**kwargs)
        context['wts'] = Order.objects.filter(want='S').order_by('-date_created').exclude(is_active=False)[:25]
        context['wtb'] = Order.objects.filter(want='B').order_by('-date_created').exclude(is_active=False)[:25]
        return context

class MarketBeast(TemplateView):
    template_name = 'market/market.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(MarketBeast, self).get_context_data(**kwargs)
        context['wts'] = Order.objects.filter(want='S').order_by('-date_created').exclude(Q(item__tipe=1) | Q(item__tipe=2) | Q(item__tipe=3))[:25]
        context['wtb'] = Order.objects.filter(want='B').order_by('-date_created').exclude(Q(item__tipe=1) | Q(item__tipe=2) | Q(item__tipe=3))[:25]
        return context

#class ItemDetail(DetailView):
#    model = Item
#    template_name = "item_detail.html"
#    pk_url_kwarg = "item_id"
#    slug_url_kwarg = 'slug'
#    query_pk_and_slug = True

#    def get_context_data(self, *args, **kwargs):
#        context = super(ItemDetail, self).get_context_data(**kwargs)
#        context['wts'] = Order.objects.all().filter(item=self.get_object(), want='S').exclude(is_active=False)
#        context['wtb'] = Order.objects.all().filter(item=self.get_object(), want='B').exclude(is_active=False)
        #context['childs'] = Item.objects.filter(parent=self.get_object())
#        return context

# Order: Create View
# Description: Used to create a new order.
class OrderCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderForm
    success_url = reverse_lazy('market')
    template_name = 'market/forms/order_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return super().form_valid(form)

# Order: Create View
# Description: Used to create a new order.
class OrderBeastCreateView(LoginRequiredMixin, CreateView):
    form_class = OrderFormBeast
    success_url = reverse_lazy('market')
    template_name = 'market/forms/order_beast_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return super().form_valid(form)