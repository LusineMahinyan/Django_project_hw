from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Создание групп"

    def handle(self, *args, **options):

        moderator_group, created = Group.objects.get_or_create(
            name="Модератор продуктов"
        )

        permissions = Permission.objects.filter(
            codename__in=[
                "can_unpublish_product",
                "delete_product",
            ]
        )

        moderator_group.permissions.set(permissions)

        self.stdout.write(
            self.style.SUCCESS(
                "Группа успешно создана"
            )
        )
