# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Faces(models.Model):

    person_name = models.CharField(max_length=200)
    cam_id = models.CharField(max_length=100, null=True, blank=True)
    cam_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
