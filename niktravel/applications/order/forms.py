from django_countries.widgets import CountrySelectWidget

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    """Form definition for Order."""

    class Meta:
        """Meta definition for Orderform."""

        model = Order
        fields = (
            'full_name',
            'email',
            'postal_code',
            'country',
        )
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form__input'
                } 
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form__input'
                }
            ),
            'postal_code': forms.TextInput(
                attrs={
                    'class': 'form__input'
                }
            ),
        }
        
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget.attrs.update({'class': 'form__input'})


