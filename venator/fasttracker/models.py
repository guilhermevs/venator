from django.db import models
from django.core.urlresolvers import reverse as r


class Bug(models.Model):
    """
    """
    STATUS = (
        ("PE", "Pending"),
        ("WO", "Working"),
    )
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=30)
    status = models.CharField(max_length=2, choices=STATUS, default="PE")

    def get_absolute_url(self):
        return r("fasttracker:bugdetail", args=(self.id,))
