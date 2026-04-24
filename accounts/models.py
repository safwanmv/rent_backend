from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("owner", "Owner"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="owner")
    created_by = models.ForeignKey(  # ← add this
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="created_users",
    )
