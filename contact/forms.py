# flake8: noqa
from django import forms
from . import models
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'imge/*'
            }
        )
    )
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',         
            'email', 'description', 'category',
            'picture'
        )       
