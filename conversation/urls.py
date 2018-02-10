# -*- coding: utf-8 -*-
from django.urls import path

from . import conv

urlpatterns = [
    path('shot', conv.shot, name='shot'),
]
