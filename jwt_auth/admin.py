from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_verified', 'otp', 'is_staff')
    list_filter = ('is_verified', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    readonly_fields = ('otp',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_verified', 'otp')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
