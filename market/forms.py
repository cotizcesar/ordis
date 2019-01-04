from django import forms

# Codex: Importing Models
from codex.models import Item

# Models
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        want = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.RadioSelect, empty_label=None)
        fields = ('item', 'want', 'price', 'quantity')
        widgets = {'want': forms.RadioSelect}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(is_tradeable=True).exclude(tipe=4)

class OrderFormBeast(forms.ModelForm):
    class Meta:
        model = Order
        want = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.RadioSelect, empty_label=None)
        fields = ('item', 'want', 'image', 'price', 'quantity')
        widgets = {'want': forms.RadioSelect}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.filter(tipe=4).exclude(is_tradeable=False)