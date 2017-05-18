# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here


def index(request):
    context = {}
    return render(request, 'app/example.html', context)


def clm_video(request):
    context = {}
    return render(request, 'app/clm_video.html', context)
