from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse

def home(request):
    data = {}
    return render(request, 'fbcalendar/home.html', data)

def add(request):
    data = {}
    return render(request, 'fbcalendar/add.html', data)

def activity_add(request):
    data = {}
    return HttpResponseRedirect(reverse("calendar_home"))

def download(request):
    data = {}
    return HttpResponseRedirect(reverse("calendar_home"))

def dayplan(request, day):
    data = {}
    return render(request, 'fbcalendar/dayplan.html', data)

def weekplan(request, day):
    data = {}
    return render(request, 'fbcalendar/weekplan.html', data)