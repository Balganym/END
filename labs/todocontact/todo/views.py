# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, QueryDict, HttpResponseRedirect
from .models import Todo, Contacts
from django.views.decorators.csrf import csrf_exempt


def index(request):
  return render(request, 'todo/index.html')

def todo(request):
  todos = Todo.objects.filter(status=False)
  done = Todo.objects.filter(status=True)
  context = {'todos': todos, 'done': done}
  return render(request, 'todo/todo.html', context)

def check(request, task_id):
  task = Todo.objects.get(id=task_id)
  task.status = True
  task.save()
  return HttpResponseRedirect(reverse('index', args=()))

@csrf_exempt
def addTask(request):
  if(request.method == "POST"):
    data = request.POST
    todo = Todo()
    todo.task = unicode(data["task"])
    todo.status = data["status"]
    todo.save()
    return HttpResponseRedirect(reverse('index', args=()))
  else:
    return HttpResponse('')

def contacts(request):
  context = {'contacts': Contacts.objects.order_by('id')}
  return render(request, 'todo/contacts.html', context)

@csrf_exempt
def addNumber(request):
  if(request.method == "POST"):
    data = request.POST
    cont = Contacts()
    cont.name = unicode(data["name"])
    cont.number = data["number"]
    cont.save()
    return HttpResponseRedirect(reverse('contacts', args=()))
  else:
    return HttpResponse('')



