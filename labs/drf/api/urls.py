from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^todos/$', views.todos, name='todos'),
  url(r'^todos/(?P<todo_id>[0-9]+)/$', views.todo_detail, name="todo_detail"),
  url(r'^contacts/$', views.contacts, name='contacts'),
  url(r'^contacts/(?P<contact_id>[0-9]+)/$', views.contact_detail, name="contact_detail"),
]
