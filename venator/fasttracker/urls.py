# coding: utf-8
from django.conf.urls import patterns, url
from venator.fasttracker.views import Index, NewBug, BugDetail


urlpatterns = patterns(
    'venator.fasttracker.views',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^new/$', NewBug.as_view(), name='newbug'),
    url(r'^(?P<pk>\d+)/', BugDetail.as_view(), name='bugdetail')
)
