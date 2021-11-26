from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_product", views.create_product, name="create_product"),
    path("ajax_add_product/", views.ajax_add_product, name="ajax_add_product"),
]