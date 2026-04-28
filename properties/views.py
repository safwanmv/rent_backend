from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room, Category, Customer
from .serializers import RoomSerializer, CategorySerializer, CustomerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class CategoryListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            category = get_object_or_404(Category, id=id, owner=request.user)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        category = Category.objects.filter(owner=request.user)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                {
                    "message": "Category created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        category = get_object_or_404(Category, id=id, owner=request.user)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Category updated successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors)

    def delete(self, request, id=None):
        category = get_object_or_404(Category, id=id, owner=request.user)
        category.delete()
        return Response(
            {"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


# ------------------------------------------------------------------------------------#


class RoomListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            room = get_object_or_404(Room, id=id, owner=request.user)
            serializer = RoomSerializer(room)
            return Response(serializer.data)

        room = Room.objects.filter(owner=request.user)
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                {
                    "message": "Room created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        room = get_object_or_404(Room, id=id, owner=request.user)
        serializer = RoomSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Room updated  successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors)

    def delete(self, request, id):
        room = get_object_or_404(Room, id=id, owner=request.user)
        room.delete()
        return Response(
            {"message": "Room Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
        )


# -------------------------------------------------------------------------------------#


class CustomerListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            customer = get_object_or_404(Customer, id=id, owner=request.user)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        customer = Customer.objects.filter(owner=request.user)
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                {
                    "message": "Customer created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors)

    def patch(self, request, id=None):
        customer = get_object_or_404(Customer, id=id, owner=request.user)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Customer updated successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors)

    def delete(self, request, id=None):
        customer = get_object_or_404(Customer, id=id, owner=request.user)
        customer.delete()
        return Response(
            {"message": "Customer Deleted Sucessfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
