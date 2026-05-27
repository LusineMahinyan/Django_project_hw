from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
)

from catalog.models import Product


class HomeListView(ListView):

    model = Product

    template_name = "catalog/home.html"

    context_object_name = "products"


class ContactsTemplateView(TemplateView):

    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):

    model = Product

    template_name = "catalog/product_detail.html"

    context_object_name = "product"


class ProductCreateView(CreateView):

    model = Product

    fields = [
        "name",
        "description",
        "image",
        "category",
        "price",
    ]

    template_name = "catalog/product_form.html"

    success_url = reverse_lazy("catalog:home")