from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    home,
    contacts,
    product_detail,
    product_create,
    product_update,
    product_delete,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),

    path("contacts/", contacts, name="contacts"),

    path(
        "products/<int:pk>/",
        product_detail,
        name="product_detail",
    ),

    path(
        "product/create/",
        product_create,
        name="product_create",
    ),

    path(
        "product/update/<int:pk>/",
        product_update,
        name="product_update",
    ),

    path(
        "product/delete/<int:pk>/",
        product_delete,
        name="product_delete",
    ),
]
