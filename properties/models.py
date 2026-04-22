import uuid
from django.db import models


def generate_id(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"


class Category(models.Model):
    category_id = models.CharField(unique=True, max_length=20, blank=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.category_id:
            self.category_id = generate_id("CAT")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_id = models.CharField(max_length=20, unique=True, blank=True)
    name = models.CharField(max_length=100)
    rent = models.FloatField()
    advance_amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.room_id:
            self.room_id = generate_id("ROOM")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True, blank=True)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    rent_amount = models.FloatField()
    advance_amount = models.FloatField()
    joined_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.customer_id:
            self.customer_id = generate_id("CUST")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_name
