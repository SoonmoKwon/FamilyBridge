from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'mainpage.views.home', name='mainpage_home'),
    url(r'^add/$', 'mainpage.views.add', name='mainpage_add'),

)
