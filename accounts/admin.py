from django.contrib import admin
from .models import User


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_active", "is_staff")
    search_fields = ("username",)


admin.site.register(User, CustomUserAdmin)
