__author__ = 'cloud'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'expense.views.home', name='expense_home'),
    url(r'^add/$', 'expense.views.add', name='expense_add'),
    url(r'^item/add/$', 'expense.views.item_add', name='expense_item_add'),
    url(r'^download/$', 'expense.views.download', name='expense_download'),
    url(r'^sort/(?P<category_name>[a-z_]+)/$', 'expense.views.sort_by_category_name', name='expense_category_name_sort'),
    url(r'^sort/(?P<category_id>[0-9]+)/$', 'expense.views.sort_by_category_id', name='expense_category_id_sort'),
    url(r'^sort/(?P<teammate_name>[a-z_]+)/$', 'expense.views.sort_by_teammate_name', name='expense_teammate_name_sort'),
    url(r'^sort/(?P<teammate_id>[0-9]+)/$', 'expense.views.sort_by_teammate_id', name='expense_teammate_id_sort'),
    url(r'^filter/(?P<category_name>[a-z_]+)/$', 'expense.views.filter_by_category_name', name='expense_category_name_filter'),
    url(r'^filter/(?P<category_id>[0-9]+)/$', 'expense.views.filter_by_category_id', name='expense_category_id_filter'),
    url(r'^filter/(?P<teammate_name>[a-z_0-9]+)/$', 'expense.views.filter_by_teammate_name', name='expense_teammate_name_filter'),
    url(r'^filter/(?P<teammate_id>[0-9]+)/$', 'expense.views.filter_by_teammate_id', name='expense_teammate_id_filter'),
    url(r'^piechart', 'expense.views.piechart', name='expense_piechart')

)
