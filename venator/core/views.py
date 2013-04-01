# Create your views here.

from django.views.generic import TemplateView
from django.shortcuts import render_to_response


class Homepage(TemplateView):
    template_name = "index.html"


def pages(request, page):
    return render_to_response(page + ".html")
