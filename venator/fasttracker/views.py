# coding: utf-8

from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "fasttracker/index.html"


class NewBug(TemplateView):
    template_name = "fasttracker/newbug.html"
