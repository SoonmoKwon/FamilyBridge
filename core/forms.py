from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


class SignUpForm(ModelForm):
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']
