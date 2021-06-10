from django.forms import ModelForm

from staff.models import ItemInCart, Order


class ItemInCartForm(ModelForm):
    class Meta:
        model = ItemInCart
        fields = ['quantity']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['payment']
