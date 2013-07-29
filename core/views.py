from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from core.forms import UserForm
from core.forms import SignUpForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    data = {}
    if not request.user.is_authenticated():
        data['login_form'] = UserForm()
        data['signup_form'] = SignUpForm()
    else:
        return HttpResponseRedirect(reverse('expense_home'))
    return render(request, 'core/home.html', data)

def signin(request):
    data = {}

    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'success')
                return HttpResponseRedirect(reverse('expense_home'))
            else:
                messages.debug(request, 'Inactive User')
        else:
            messages.error(request, 'Invalid username')
    data['login_form'] = UserForm(request.POST or None)
    data['signup_form'] = SignUpForm(request.POST or None)
    return render(request, 'core/home.html', data)

def signout(request):
    data = {}
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def email_check(request):
    data = {}
    data['login'] = '0'
    if User.objects.get(email = request.POST["username"]):
        data['login'] = 'Error: Already registerd email'
    return render(request, 'core/home.html', data)

def signup(request):
    data = {}
    data['login'] = '0'
    if request.method == "POST":
        if request.POST["password"] != request.POST["password2"]:
            data['login'] = '1'
            messages.error(request, 'Passwords are different')
        if not (request.POST["email_check"]):
            data['login'] = '1'
            messages.error(request, 'Invalid Email')
    if data['login'] == '0':
        data['form'] = SignUpForm(request.POST)
        if data['form'].is_valid():
            data['form'].save()
        else:
            messages.error(request, 'Check Your Email')
    return render(request, 'core/home.html', data)

def forgot_password(request):
    data = {}
    if request.method == "POST":
        send_mail('Your Password', 'Here is your password:' + request.POST["email"], 'admin@familybranch.com', ["request.POST['email']"], false_silently=False)
    return render(request, 'core/home.html', data)
