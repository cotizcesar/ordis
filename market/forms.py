from django import forms

# Models
from .models import Item, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        want = forms.ModelChoiceField(queryset=Item.objects.all(), widget=forms.RadioSelect, empty_label=None)
        fields = ('item', 'want', 'price', 'quantity', 'mod_rank')
        widgets = {'want': forms.RadioSelect}