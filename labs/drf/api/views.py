from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from .models import Todo, Contacts
from .serializers import TodoSerializer, ContactSerializer

@csrf_exempt
def todos(request):
  if request.method == "GET":
    todos = Todo.objects.all()
    ser = TodoSerializer(todos, many=True)
    return JsonResponse(ser.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    ser = TodoSerializer(data=data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data, status=201)
    return JsonResponse(ser.errors, status=400)


@csrf_exempt
def todo_detail(request, todo_id):
  try:
    todo = Todo.objects.get(id=todo_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    ser = TodoSerializer(todo)
    return JsonResponse(ser.data) 
  elif request.method == "PUT":
    data = JSONParser().parse(request)
    ser = TodoSerializer(todo, data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data)
    return HttpResponse('error data')
  elif request.method == "DELETE":
    todo.delete()
    ser = TodoSerializer(todo)
    return JsonResponse(ser.data)


@csrf_exempt
def contacts(request):
  if request.method == "GET":
    contacts = Contacts.objects.all()
    ser = ContactSerializer(contacts, many=True)
    return JsonResponse(ser.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    ser = ContactSerializer(data=data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data, status=201)
    return JsonResponse(ser.errors, status=400)


@csrf_exempt
def contact_detail(request, contact_id):
  try:
    contact = Contacts.objects.get(id=contact_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    ser = ContactSerializer(contact)
    return JsonResponse(ser.data) 
  elif request.method == "PUT":
    data = JSONParser().parse(request)
    ser = ContactSerializer(contact, data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data)
  elif request.method == "DELETE":
    contact.delete()
    ser = ContactSerializer(contact)
    return JsonResponse(ser.data)










