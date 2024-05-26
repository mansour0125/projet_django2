from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Apprenant

class ApprenantForm(forms.ModelForm):

    class Meta:

        model=Apprenant
        fields= "__all__"


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requis. Entrez une adresse e-mail valide.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')