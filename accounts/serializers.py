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
        created_by = validated_data.pop("created_by", None)  # ← extract it
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        user.role = validated_data.get("role", "owner")
        user.created_by = created_by  # ← assign it
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(
        source="created_by.username", read_only=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "role",
            "created_by_username",
            "date_joined",
            "is_active",
        ]
        extra_kwargs = {
            "email": {
                "required": False,
                "allow_null": True,
                "allow_blank": True,
            },
            "username": {"required": False},
        }
