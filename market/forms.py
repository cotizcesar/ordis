from django import forms

# Codex: Importing Models
from codex.models import Item

# Models
from .models import Order

class OrderForm(forms.ModelForm):
    #form.base_fields['item'].queryset = Item.objects.filter(is_tradeable=True)
    class Meta:
        model = Order
        want = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.RadioSelect, empty_label=None)
        fields = ('item', 'want', 'price', 'quantity', 'mod_rank')
        widgets = {'want': forms.RadioSelect}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(is_tradeable=True)