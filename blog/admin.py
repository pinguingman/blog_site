from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Blog_record, User


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email']
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'subscriptions', 'seen_posts')
        }),
    )


admin.site.register(Blog_record)
admin.site.register(User, CustomUserAdmin)
