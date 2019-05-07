from django.contrib import admin
from .models import Blog_record, User


class User_record_admin(admin.ModelAdmin):
    fields = ['username', 'password', 'email', 'subscriptions', 'seen_posts']


admin.site.register(Blog_record)
admin.site.register(User, User_record_admin)
