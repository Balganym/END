# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

  def to_json(self):
    return{
      "id": self.id,
      "name": self.name
    }

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
  name = models.CharField(max_length=200)
  price = models.FloatField(default=0.0)

  def __str__(self):
    return self.name

  def to_json(self):
    return{
      "id": self.id,
      "name": self.name,
      "price": self.price,
      "category": self.category.to_json()
    }