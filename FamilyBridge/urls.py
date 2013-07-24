from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('core.urls')),
    # url(r'^FamilyBridge/', include('FamilyBridge.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calendar/', include('fbcalendar.urls')),
    url(r'^expense/', include('expense.urls')),
    url(r'^home/', include('core.urls')),
)
