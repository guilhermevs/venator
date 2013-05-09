# coding: utf-8

from django import forms
from venator.fasttracker.models import Bug


class BugForm(forms.Form):
    class Meta:
        model = Bug
