# coding: utf-8
from django.conf.urls import patterns, url
from venator.fasttracker.views import Index, NewBug


urlpatterns = patterns(
    'venator.fasttracker.views',
    url(r'^$', Index.as_view(), name='homepage'),
    url(r'^new/$', NewBug.as_view(), name='newbug'),
)
