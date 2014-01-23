"""Urls for emencia-django-socialaggregator"""
from django.conf.urls import url, patterns

from views import RessourceListView
from views import RessourceByFeedListView

urlpatterns = patterns(
    '',
    url(r'^feed/(?P<slug>[-\w]+)/$', RessourceByFeedListView.as_view(),
        name='socialaggregator_ressource_by_feed_list_view'),
    url(r'^$', RessourceListView.as_view(),
        name='socialaggregator_ressource_list_view'),
    )
