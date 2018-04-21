# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):
  task = models.CharField(max_length = 200)
  status = models.BooleanField(default=False)


class Contacts(models.Model):
  name = models.CharField(max_length = 200)
  number = models.CharField(max_length = 200)