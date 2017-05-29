from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Entry(models.Model):
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_updated']
