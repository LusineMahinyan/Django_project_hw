from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

from catalog.models import Product
from catalog.forms import ProductForm


def home(request):

    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(
        request,
        "catalog/home.html",
        context,
    )


def contacts(request):

    return render(
        request,
        "catalog/contacts.html",
    )


def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    context = {
        "product": product,
    }

    return render(
        request,
        "catalog/product_detail.html",
        context,
    )


@login_required
def product_create(request):

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "catalog:home"
            )

    else:

        form = ProductForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "catalog/product_form.html",
        context,
    )


@login_required
def product_update(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

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

    context = {
        "form": form,
    }

    return render(
        request,
        "catalog/product_form.html",
        context,
    )


@login_required
def product_delete(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    if request.method == "POST":

        product.delete()

        return redirect(
            "catalog:home"
        )

    context = {
        "product": product,
    }

    return render(
        request,
        "catalog/product_confirm_delete.html",
        context,
    )
