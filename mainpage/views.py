# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from expense.forms import ExpenseItemForm
from expense.models import Item
from core.models import Category

def home(request):
    data = {}
    return render(request, 'mainpage/home.html', data)

def add(request):
    data = {}
    form = ExpenseItemForm(request.POST or None)
    Category.objects.get_or_create(name = 'doctor')
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'expense/add.html', data)

