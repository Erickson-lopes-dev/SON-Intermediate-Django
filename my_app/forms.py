from django import forms
from .models import STATES_CHOICES


class AddressForm(forms.Form):
    address = forms.CharField(max_length=255,
                              widget=forms.TextInput(attrs={'class': 'form-control'})
                              )
    # campo não requerido
    address_complement = forms.CharField(max_length=255,
                                         widget=forms.TextInput(attrs={'class': 'form-control'}),
                                         required=False
                                         )
    city = forms.CharField(max_length=255,
                           widget=forms.TextInput(attrs={'class': 'form-control'})
                           )
    state = forms.ChoiceField(choices=STATES_CHOICES,
                              widget=forms.Select(attrs={'class': 'form-control'})
                              )

    contry = forms.CharField(max_length=255,
                             widget=forms.TextInput(attrs={'class': 'form-control'})
                             )
