from django.conf.urls import url

from . import views


urlpatterns = [
  url(r'^products/', views.products ,name='products'),
  url(r'^(?P<category_id>[0-9]+)/', views.category_product,
    name='category_product'),
  url(r'^(?P<prod_id>[0-9]+)/', views.product_detail,
    name='product_detail')
]