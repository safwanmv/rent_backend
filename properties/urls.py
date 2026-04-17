from django.urls import path
from .views import (
    RoomListCreateAPIView,
    CategoryListCreateAPIView,
    CustomerListCreateAPIView,
)


urlpatterns = [
    path("room/", RoomListCreateAPIView.as_view()),
    path("room/<int:id>", RoomListCreateAPIView.as_view()),
    path("category/", CategoryListCreateAPIView.as_view()),
    path("category/<int:id>", CategoryListCreateAPIView.as_view()),
    path("customer/", CustomerListCreateAPIView.as_view()),
    path("customer/<int:id>", CustomerListCreateAPIView.as_view()),
]
