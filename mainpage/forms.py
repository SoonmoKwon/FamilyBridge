from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, PasswordInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'password': PasswordInput()
        }


class SignUpForm(ModelForm):
    password2 = forms.CharField(max_length = 30, widget= PasswordInput)
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']
        widgets = {
            'password': PasswordInput()
        }
