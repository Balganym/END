# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, QueryDict, HttpResponseRedirect

from .models import Category, Product
from django.views.decorators.csrf import csrf_exempt

def categories(request):
  if request.method == "GET":
    context = {'categories': Category.objects.all()}
    return render(request, 'demo/index.html', context)

def category_detail(request, category_id):
  try:
    category = Category.objects.get(id=category_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    res = Product.objects.filter(category=category)
    context = {'products': res, 'c_id': category_id}
    return render(request, 'demo/products.html', context)
  elif request.method == "POST":
    data = request.POST
    prod = Product()
    prod.category = category
    prod.name = data.get("name", prod.name)
    prod.price = data.get("price", prod.price)
    prod.save()
    res = Product.objects.filter(category=category)
    context = {'products': res, 'c_id': category_id}
    return render(request, 'demo/products.html', context)

def product_detail(request, prod_id):
  try:
    prod = Product.objects.get(id=prod_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    context = {'product': prod}
    return render(request, 'demo/product.html', context)
  elif request.method == "POST":
    data = request.POST
    category_name = data.get("category", prod.category)
    category, _ = Category.objects.get_or_create(name=category_name)
    prod.category = category
    prod.name = data.get("name", prod.name)
    prod.price = data.get("price", prod.price)
    prod.save()
    return HttpResponseRedirect(reverse('product_detail', args=(prod_id)))

def delete(request, prod_id):
  try:
    prod = Product.objects.get(id=prod_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  prod.delete()
  return HttpResponseRedirect(reverse('category_detail', args=(prod_id)))




