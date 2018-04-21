# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):
  title = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now=True)
  status = models.BooleanField(default=False)

  def __str__(self):
    return self.title

class Contacts(models.Model):
  name = models.CharField(max_length=200)
  number = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title