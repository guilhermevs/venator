# coding: utf-8

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from venator.fasttracker.models import Bug


class Index(ListView):
    # def get(self, request):
    #     if "order" in request.GET:
    #     return super(Index, self).get(request)

    queryset = Bug.objects.exclude(status="DE")

    model = Bug
    template_name = "fasttracker/index.html"


class NewBug(CreateView):
    model = Bug


class BugDetail(DetailView):
    model = Bug
