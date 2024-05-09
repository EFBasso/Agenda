# flake8: noqa
from django import forms
from . import models
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
         widget=forms.TextInput({
            'class':'classe-a classe-b',
            'placeholder': 'Alterando o campo'
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda',
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',         
            'email', 'description', 'category'
        )       

    # def clean(self):       
    #     self.add_error(
    #         'first_name',
    #         ValidationError(
    #             'Mensagem de erro',
    #             code='invalid',
    #         )
    #     )
    #     return super().clean()