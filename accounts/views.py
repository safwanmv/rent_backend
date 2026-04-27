from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    CustomTokenObtainPairSerializer,
    UserCreateSerializer,
    UserListSerializer,
)
from .models import User


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CreateUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("USER:", request.user)
        print("ROLE:", request.user.role)
        if request.user.role != "admin":
            return Response(
                {
                    "error": "only admin can create users",
                },
                status=403,
            )
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DashboardStatsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            if user.role == "admin":
                users_created = User.objects.filter(created_by=user).count()
                return Response(
                    {
                        "role": "admin",
                        "stats": {
                            "users_created": users_created,
                        },
                    }
                )

            elif user.role == "owner":
                return Response({"role": "owner", "stats": {}})

            return Response({"error": "Unknown role"}, status=400)

        except Exception as e:
            return Response({"error": str(e)}, status=500)  # ← will show exact error


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != "admin":
            return Response({"error": "Access denied"}, status=403)

        users = User.objects.filter(role="owner").order_by("-date_joined")
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
