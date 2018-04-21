from rest_framework import serializers

from .models import Todo, Contacts

class TodoSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Todo
    fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Contacts
    fields = "__all__"
