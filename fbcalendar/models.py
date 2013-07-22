from django.db import models
from django.contrib.auth.models import User
from core.models import Category

class Activity (models.Model):
    team_member = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)