from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    home,
    contacts,
    product_detail,
    product_create,
    product_update,
    product_delete,
    category_products,
)

app_name = CatalogConfig.name

urlpatterns = [
    path(
        "",
        cache_page(60 * 5)(home),
        name="home",
    ),

    path(
        "contacts/",
        contacts,
        name="contacts",
    ),

    path(
        "products/<int:pk>/",
        cache_page(60 * 5)(product_detail),
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

    path(
        "category/<int:category_id>/",
        cache_page(60 * 10)(category_products),
        name="category_products",
    ),
]
