from django import forms
from .models import STATES_CHOICES


class AddressForm(forms.Form):
    address = forms.CharField(max_length=255)
    # campo não requerido
    address_complement = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=255)
    state = forms.ChoiceField(choices=STATES_CHOICES)
    contry = forms.CharField(max_length=255)
