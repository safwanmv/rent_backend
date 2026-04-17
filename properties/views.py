from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room, Category, Customer
from .serializers import RoomSerializer, CategorySerializer, CustomerSerializer
from django.shortcuts import get_object_or_404


class RoomListCreateAPIView(APIView):

    def get(self, request, id=None):
        if id:
            room = get_object_or_404(Room, id=id)
            serializer = RoomSerializer(room)
            return Response(serializer.data)

        room = Room.objects.all()
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        room = get_object_or_404(Room, id=id)
        serializer = RoomSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        room = get_object_or_404(Room, id=id)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------------------------------------------------------------------------#


class CategoryListCreateAPIView(APIView):
    def get(self, request, id=None):
        if id:
            category = get_object_or_404(Category, id=id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, reqeust, id=None):
        category = get_object_or_404(Category, id=id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------------------------------------------------------------#


class CustomerListCreateAPIView(APIView):
    def get(self, request, id=None):
        if id:
            customer = get_object_or_404(Customer, id=id)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def patch(self, request, id=None):
        customer = get_object_or_404(Customer, id=id)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id=None):
        customer = get_object_or_404(Customer, id=id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
