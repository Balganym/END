# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from .models import Todo, Contacts

@csrf_exempt
def todos(request):
  if request.method == "GET":
    todos = Todo.objects.all()
    todo_json = [t.to_json() for t in todos]
    return JsonResponse(todo_json, safe=False)
  elif request.method == "POST":
    data = request.POST
    todo = Todo()
    todo.task = data.get("task", "")
    todo.save()
    
    return JsonResponse(todo.to_json(), status=201)

@csrf_exempt
def todo_detail(request, todo_id):
  try:
    todo = Todo.objects.get(id=todo_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    return JsonResponse(todo.to_json(), safe=False)
  elif request.method == "PUT":
    data = QueryDict(request.body)
    todo.task = data.get('task', todo.task)
    todo.status = data.get('status', todo.status)
    todo.save()
    return JsonResponse(todo.to_json())
  elif request.method == "DELETE":
    todo.delete()
    return JsonResponse(todo.to_json())


@csrf_exempt
def contacts(request):
  if request.method == "GET":
    contacts = Contacts.objects.all()
    contact_json = [c.to_json() for c in contacts]
    return JsonResponse(contact_json, safe=False)
  elif request.method == "POST":
    data = request.POST
    contact = Contacts()
    contact.name = data.get("name", "")
    contact.number = data.get("number", "")
    contact.save()
    
    return JsonResponse(contact.to_json())

@csrf_exempt
def contact_detail(request, contact_id):
  try:
    contact = Contacts.objects.get(id=contact_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    return JsonResponse(contact.to_json(), safe=False)
  elif request.method == "PUT":
    data = QueryDict(request.body)
    contact.name = data.get('name', contact.name)
    contact.number = data.get('number', contact.number)
    contact.save()
    return JsonResponse(contact.to_json())
  elif request.method == "DELETE":
    contact.delete()
    return JsonResponse(contact.to_json())


  