from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from fbcalendar.forms import ActivityForm
from fbcalendar.models import Activity
from core.models import Category

def home(request):
    data = {}
    data['form'] = Activity.objects.all()
    return render(request, 'fbcalendar/home.html', data)

def add(request):
    data = {}
    Category.objects.get_or_create(name = 'food')
    data['form'] = ActivityForm()
    return render(request, 'fbcalendar/add.html', data)

def activity_add(request):
    data = {}
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
        data['form'] = form
    return render(request, 'fbcalendar/add.html', data)

def download(request):
    data = {}
    return HttpResponseRedirect(reverse("calendar_home"))

def dayplan(request, day):
    data = {}
    return render(request, 'fbcalendar/dayplan.html', data)

def weekplan(request, day):
    data = {}
    return render(request, 'fbcalendar/weekplan.html', data)