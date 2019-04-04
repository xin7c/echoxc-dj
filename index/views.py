# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    meta = request.META
    REMOTE_ADDR = meta["REMOTE_ADDR"]
    
    return render(request, 'home.html', {"REMOTE_ADDR": REMOTE_ADDR})
