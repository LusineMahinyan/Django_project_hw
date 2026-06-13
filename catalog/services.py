from django.core.cache import cache
from django.shortcuts import get_object_or_404

from catalog.models import Product


def get_product_by_pk(pk):

    cache_key = f"product_{pk}"

    product = cache.get(cache_key)

    if product is None:

        product = get_object_or_404(
            Product,
            pk=pk,
        )

        cache.set(
            cache_key,
            product,
            60 * 5,
        )

    return product


def get_products_by_category(category_id):

    cache_key = f"category_{category_id}"

    products = cache.get(cache_key)

    if products is None:

        products = list(
            Product.objects.filter(
                category_id=category_id
            )
        )

        cache.set(
            cache_key,
            products,
            60 * 10,
        )

    return products
