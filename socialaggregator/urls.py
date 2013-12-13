"""Urls for emencia-django-socialaggregator"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from views import RessourceListView

urlpatterns = patterns(
    '',
    url(r'^$', RessourceListView.as_view(),
        name='socialaggregator_ressource_list_view'),
    )
