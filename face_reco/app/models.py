# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


def content_file_name(instance, filename):
    return '/'.join(['static/photos/', instance.person_name, filename])


class Faces(models.Model):

    person_name = models.CharField(max_length=200)
    cam_id = models.CharField(max_length=100, null=True, blank=True)
    cam_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to=content_file_name, null=True, max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def image_thumb(self):
        return '<img src="/%s" width="100" height="100" />' % (self.image)
    image_thumb.allow_tags = True
