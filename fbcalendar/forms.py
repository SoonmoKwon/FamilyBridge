__author__ = 'cloud'
from django.forms import ModelForm
from fbcalendar.models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['team_member', 'description', 'category', 'start_time', 'end_time']