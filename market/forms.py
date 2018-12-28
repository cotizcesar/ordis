from django import forms

# Codex: Importing Models
from codex.models import Companion, Warframe, Weapon
# Models
from .models import Item, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        want = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.RadioSelect, empty_label=None)
        fields = ('item', 'want', 'price', 'quantity', 'mod_rank')
        widgets = {'want': forms.RadioSelect}