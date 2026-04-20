from django.db import models

# Create your models here.


class Category(models.Model):
    category_id = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    rent = models.FloatField()
    advance_amount = models.FloatField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True)
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100, null=True)
    address = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    rent_amount = models.FloatField()
    advance_amount = models.FloatField()
    joined_date = models.DateField()

    def __str__(self):
        return self.customer_name
