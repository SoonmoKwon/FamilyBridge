from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from core.forms import UserForm
from core.forms import SignUpForm
from django.contrib.auth.models import User

def home(request):
    data = {}
    return render(request, 'core/home.html', data)

def login(request):
    data = {}
    data['form'] = UserForm()
    return render(request, 'core/login.html', data)

def signup(request):
    data = {}
    data['form'] = SignUpForm()
    return render(request, 'core/signup.html', data)

def forgot_password(request):
    data = {}
    return render(request, 'core/home.html', data)

def about(request):
    data = {}
    return render(request, 'core/about.html', data)