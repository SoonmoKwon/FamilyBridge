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
    data['items'] = Item.objects.all()
    return render(request, 'expense/home.html', data)

def add(request):
    data = {}
    form = ExpenseItemForm(request.POST or None)
    Category.objects.get_or_create(name = 'doctor')
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'expense/add.html', data)

def item_add(request):
    data = {}
    return HttpResponseRedirect(reverse('expense_home'))

def download(request):
    data = {}
    return HttpResponseRedirect(reverse('expense_home'))

def sort_by_category_name(request, category_name):
    data = {}
    return render(request, 'expense/home.html', data)
    
def sort_by_category_id(request, category_id):
    data = {}
    return render(request, 'expense/home.html', data)    

def sort_by_teammate_name(request, teammate_name):
    data = {}
    return render(request, 'expense/home.html', data)
                  
def sort_by_teammate_id(request, teammate_id):
    data = {}
    return render(request, 'expense/home.html', data)    

def filter_by_category_name(request, category_name):
    data = {}
    return render(request, 'expense/home.html', data)
    
def filter_by_category_id(request, category_id):
    data = {}
    return render(request, 'expense/home.html', data)    

def filter_by_teammate_name(request, teammate_name):
    data = {}
    return render(request, 'expense/home.html', data)
                  
def filter_by_teammate_id(request, teammate_id):
    data = {}
    return render(request, 'expense/home.html', data)    