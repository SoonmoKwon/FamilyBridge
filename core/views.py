from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from core.forms import UserForm
from core.forms import SignUpForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.template import RequestContext
from premailer import Premailer
from django.core.mail import EmailMultiAlternatives

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
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password"] == form.cleaned_data["password2"]:
                user = form.save()
                user.set_password(form.cleaned_data['password'])
                user.save()
                user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data['password'])
                if user.is_active:
                    login(request, user)
                else:
                    user.is_active = True
                    user.save()
                    login(request, user)
                    messages.warning(request, "User has been automatically activated")
                title = 'Dear %s' % (user.first_name, )
                contents = 'You can manage your care giving expenses through FamilyBridge'
                html_msg = render_to_string("email/index.html", RequestContext(request,
                    {'title': title, 'contents': contents }))

                p = Premailer(html_msg)
                html_msg = p.transform()

                msg = EmailMultiAlternatives('Welcome to FamilyBridge', title+contents, 'asifiloveu@gmail.com', [user.email])
                msg.attach_alternative(html_msg, 'text/html')
                msg.send()
                return HttpResponseRedirect(reverse('expense_home'))
            else:
                messages.error(request, 'Your passwords do not match')
    print request.POST
    print form
    data['login_form'] = UserForm()
    data['signup_form'] = form
    return render(request, 'core/home.html', data)

def forgot_password(request):
    data = {}
    if request.method == "POST":
        send_mail('Your Password', 'Here is your password:' + request.POST["email"], 'admin@familybranch.com', ["request.POST['email']"], false_silently=False)
    return render(request, 'core/home.html', data)
