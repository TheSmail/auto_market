from django import forms
from .models import *
from django.forms import HiddenInput, CharField
from bootstrap_modal_forms.forms import BSModalModelForm

class ProductForm(BSModalModelForm):
    class Meta:
        fields = ['product_name', 'vendor_code', 'contractor', 'price']
        model = Product

class OrderItemForm(forms.ModelForm):
    class Meta:
        fields = ['quantity', 'markup']
        model = OrderItem

class OrderForm(forms.ModelForm):
    # client = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        fields = ('note',)
        model = Order