from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 64)
    creation_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return "%s"%(self.name.capitalize(),)