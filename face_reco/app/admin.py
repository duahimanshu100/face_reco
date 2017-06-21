# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import Faces


class FaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'person_name', 'created_at', 'cam_id']


admin.site.register(Faces, FaceAdmin)
