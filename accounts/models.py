from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("owner", "Owner"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="owner")
