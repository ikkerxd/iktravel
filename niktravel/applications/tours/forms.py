# django
from django import forms

class CartForm(forms.Form):
    """Cart definition."""

    quantity = forms.IntegerField(
        max_value=12,
        min_value=1,
        required=True,
        initial=1,
    )
