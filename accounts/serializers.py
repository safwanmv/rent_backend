from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        role = validated_data.get("role", "owner")
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        user.role = role
        user.save()
        return user
