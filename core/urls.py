from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^home/$', 'core.views.home', name='home'),
    url(r'^login/$', 'core.views.login', name='login'),
    url(r'^signup/$', 'core.views.signup', name='signup'),
    url(r'^email/check/$', 'core.views.email_check', name='email_check'),
    url(r'^forgot/password/$', 'core.views.forgot_password', name='forgot_password'),
)