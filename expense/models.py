from django.db import models
from django.contrib.auth.models import User
from core.models import Category

# Create your models here.

class Item(models.Model):
    activity_date = models.DateField()
    team_member = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    dollar_amount = models.DecimalField(max_digits=10, decimal_places=2)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)