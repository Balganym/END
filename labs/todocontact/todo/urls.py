from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^todo/(?P<task_id>[0-9]+)/$', views.check, name='check'),
  url(r'^todo/$', views.todo, name='todo'),
  url(r'^todo/add$', views.addTask, name='addTask'),
  url(r'^contacts/$', views.contacts, name='contacts'),
  url(r'^contacts/add$', views.addNumber, name='addNumber'),
]