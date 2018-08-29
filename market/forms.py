from django import forms

# Models
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('item', 'want', 'price', 'quantity', 'mod_rank')