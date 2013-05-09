# coding: utf-8

from django.contrib import admin
from venator.fasttracker.models import Bug


class BugAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator')

admin.site.register(Bug, BugAdmin)
