# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Todo, Contacts

admin.site.register(Todo)
admin.site.register(Contacts)
