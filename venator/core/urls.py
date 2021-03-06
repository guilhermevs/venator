# coding: utf-8
from django.conf.urls import patterns, include, url
from venator.core.views import Homepage


urlpatterns = patterns(
    'venator.core.views',
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^(?P<page>\w+)/$', 'pages', name='pages'),
    url(r'^demand/(?P<page>\w+)/$', 'pages')
)
