import os
from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = "Create or fix the superadmin user with role=admin"

    def handle(self, *args, **kwargs):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@admin.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin1234")

        user, created = User.objects.get_or_create(username=username)
        user.email = email
        user.is_superuser = True
        user.is_staff = True
        user.role = "admin"
        if created:
            user.set_password(password)
        user.save()

        self.stdout.write(f"Admin ready — role: {user.role}, created: {created}")
