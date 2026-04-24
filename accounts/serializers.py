from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["role"] = self.user.role  # 👈 add role to response
        return data


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "role",
            "created_by",
        ]  # ← add created_by
        extra_kwargs = {
            "password": {"write_only": True},
            "created_by": {"read_only": True},  # ← set by view, not request body
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        user.role = validated_data.get("role", "owner")
        user.save()
        return user
