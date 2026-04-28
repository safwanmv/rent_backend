import uuid
from django.db import models


def generate_custom_id(prefix, owner_id, last_id_str):
    if last_id_str:
        try:
            num = int(last_id_str.split("-")[-1]) + 1
        except:
            num = 1
    else:
        num = 1
    return f"{prefix}-{owner_id}-{num:03d}"


class Category(models.Model):
    category_id = models.CharField(unique=True, max_length=20, blank=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.category_id:
            last = Category.objects.filter(owner=self.owner).order_by("-id").first()
            self.category_id = generate_custom_id(
                "CAT", self.owner.id, last.category_id if last else None
            )
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
            last = Room.objects.filter(owner=self.owner).order_by("-id").first()
            self.room_id = generate_custom_id(
                "ROOM", self.owner.id, last.room_id if last else None
            )
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
            last = Customer.objects.filter(owner=self.owner).order_by("-id").first()
            self.customer_id = generate_custom_id(
                "CUST", self.owner.id, last.customer_id if last else None
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_name
