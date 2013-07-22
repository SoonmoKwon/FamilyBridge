from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'fbcalendar.views.home', name='calendar_home'),
    url(r'^/add/$', 'fbcalendar.views.add', name='calendar_add'),
    url(r'^/activity/add/$', 'fbcalendar.views.activity_add', name='calendar_activity_add'),
    url(r'^/download/$', 'fbcalendar.views.download', name='calendar_download'),
    url(r'^/(?P<day>\d{2}\d{2}\d{4})/$', 'fbcalendar.views.dayplan', name='calendar_dayplan'),
    url(r'^/week/(?P<day>\d{2}\d{2}\d{4})/$', 'fbcalendar.views.weekplan', name='calendar_weekplan'),
)
