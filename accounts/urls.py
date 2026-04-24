from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CreateUserAPIView, CustomTokenObtainPairView

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view()),  # 👈 custom view
    path("token/refresh/", TokenRefreshView.as_view()),
    path("create-user/", CreateUserAPIView.as_view()),
]
