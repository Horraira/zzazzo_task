from django import forms
from .models import User, Purchase, Payment


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ('user',)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ('user', 'purchase',)
