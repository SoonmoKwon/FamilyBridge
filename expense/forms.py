__author__ = 'cloud'

from django.db import models
from django.forms import ModelForm
from expense.models import Item

class ExpenseItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['activity_date', 'team_member', 'category', 'dollar_amount']

