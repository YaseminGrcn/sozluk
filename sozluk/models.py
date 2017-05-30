from __future__ import unicode_literals

import hashlib
from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_updated']

    def __str__(self):
        return self.title


class Post(models.Model):
    entry = models.ForeignKey(Entry)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='liked')
    dislikes = models.ManyToManyField(User, related_name='disliked')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    ip = models.GenericIPAddressField()
    reported = models.BooleanField(default=False)

    def __str__(self):
        return self.author.username

    class Meta:
        ordering = ['created', 'author']
