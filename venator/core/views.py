# Create your views here.

from django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name = "index.html"
