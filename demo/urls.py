from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^categories/$', views.categories ,name='categories'),
  url(r'^categories/(?P<category_id>[0-9]+)/$', views.category_detail,
    name='category_detail'),
  url(r'^categories/[0-9]+/(?P<prod_id>[0-9]+)/$', views.product_detail, name='product_detail'),
  url(r'^categories/[0-9]+/(?P<prod_id>[0-9]+)/delete/$', views.delete , name='delete')
]