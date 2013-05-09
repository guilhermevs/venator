from django.db import models


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
    status = models.CharField(max_length=2, choices=STATUS)
