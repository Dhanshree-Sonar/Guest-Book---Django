# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'guestbook_app/index.html')

def sign(request):
    return render(request, 'guestbook_app/sign.html')
