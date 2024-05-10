# flake8: noqa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

from . import models


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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
    )


    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Este e-mail já foi cadastrado', code='invalid')
            )

        return email
    
class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )