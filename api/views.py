# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict

from .models import Category, Product
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def products(request):
  if request.method == "GET":
    products = Product.objects.all()
    data = [p.to_json() for p in products]
    return JsonResponse(data, safe=False)
  elif request.method == "POST":
    data = request.POST
    prod = Product()
    category_name = data.get("category", "")
    category, _ = Category.objects.get_or_create(name=category_name)
    prod.category = category
    prod.name = data.get("name", "")
    prod.price = data.get("price", "")

    return JsonResponse(prod.to_json())

@csrf_exempt
def category_product(request, category_id):

  try:
    category = Category.objects.get(id=category_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    res = Product.objects.filter(category=category)
    data = [r.to_json() for r in res]
    return JsonResponse(data, safe=False)


@csrf_exempt
def product_detail(request, prod_id):
  try: 
    prod = Product.objects.get(id=prod_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    return JsonResponse(prod.to_json(), safe=False)
  elif request.method == "PUT":
    data = QueryDict(request.body)
    category_name = data.get("category", prod.category)
    category, _ = Category.objects.get_or_create(name=category_name)
    prod.category = category
    prod.name = data.get("name", prod.name)
    prod.price = data.get("price", prod.price)
    prod.save()
    return JsonResponse(prod.to_json(), safe=False)
  elif request.method == "DELETE":
    prod.delete()
    return JsonResponse(prod.to_json(), safe=False)







