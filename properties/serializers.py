from rest_framework import serializers
from .models import Category, Room, Customer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            "owner": {"read_only": True},
            "category_id": {"read_only": True},  # 👈 auto-generated
        }


class RoomSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Room
        fields = [
            "id",
            "room_id",
            "name",
            "rent",
            "advance_amount",
            "category",
            "category_name",
        ]
        extra_kwargs = {
            "room_id": {"read_only": True},
        }


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        extra_kwargs = {
            "owner": {"read_only": True},
            "customer_id": {"read_only": True},  # 👈 auto-generated
        }
