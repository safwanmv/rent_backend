from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserCreateSerializer


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
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
