from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Load test data"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        cat1 = Category.objects.create(name="Electronics", description="Tech")
        cat2 = Category.objects.create(name="Clothes", description="Wear")

        Product.objects.create(name="iPhone", price=1000, category=cat1)
        Product.objects.create(name="Laptop", price=2000, category=cat1)
        Product.objects.create(name="T-Shirt", price=20, category=cat2)

        self.stdout.write(self.style.SUCCESS("Test data loaded successfully"))
