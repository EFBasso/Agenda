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

    # Outro_campo = forms.CharField(
    #      widget=forms.TextInput({
    #         'class':'classe-a classe-b',
    #         'placeholder': 'Outro campo'
    #         }
    #     ),
    #     label='Outro campo',
    #     help_text='Texto de ajuda',
    # )

    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)

            # self.fields['first_name'].widget.attrs.update({
            #     'class':'classe-a classe-b',
            #     'placeholder': 'O texto veio do __init__'
            # })


    class Meta: 
        model = models.Contact

        fields = 'first_name', 'last_name', 'phone'
    
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'classe-a classe-b',
        #             'placeholder': 'Escreva aqui'
        #         }
        #     )
        # }
            
    
    

    def clean(self):       
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid',
            )
        )

        self.add_error(
            'last_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid',
            )
        )
        return super().clean()