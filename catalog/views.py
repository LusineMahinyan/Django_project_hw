from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Product
from catalog.forms import ProductForm
from catalog.services import (
    get_products_by_category,
    get_product_by_pk,
)


def home(request):
    products = Product.objects.all()

    return render(
        request,
        "catalog/home.html",
        {"products": products},
    )


def contacts(request):
    return render(
        request,
        "catalog/contacts.html",
    )


def product_detail(request, pk):

    product = get_product_by_pk(pk)

    return render(
        request,
        "catalog/product_detail.html",
        {"product": product},
    )


@login_required
def product_create(request):

    if request.method == "POST":
        form = ProductForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            product = form.save(
                commit=False,
            )

            product.owner = request.user

            product.save()

            return redirect(
                "catalog:home",
            )

    else:
        form = ProductForm()

    return render(
        request,
        "catalog/product_form.html",
        {"form": form},
    )


@login_required
def product_update(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    if (
        request.user != product.owner
        and not request.user.has_perm(
            "catalog.change_product"
        )
    ):
        raise PermissionDenied()

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "catalog:product_detail",
                pk=product.pk,
            )

    else:

        form = ProductForm(
            instance=product,
        )

    return render(
        request,
        "catalog/product_form.html",
        {"form": form},
    )


@login_required
def product_delete(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    if (
        request.user != product.owner
        and not request.user.has_perm(
            "catalog.delete_product"
        )
    ):
        raise PermissionDenied()

    if request.method == "POST":

        product.delete()

        return redirect(
            "catalog:home",
        )

    return render(
        request,
        "catalog/product_confirm_delete.html",
        {"product": product},
    )


def category_products(request, category_id):

    products = get_products_by_category(
        category_id,
    )

    return render(
        request,
        "catalog/category_products.html",
        {"products": products},
    )
