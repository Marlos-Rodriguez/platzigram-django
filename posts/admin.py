from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts admin"""
    list_display = ('pk', 'title', 'photo', 'user', 'profile', 'created')

    list_display_links = ('pk', 'title', 'created',)

    list_editable = ('photo',)

    search_fields = (
        'title', 'user__email', 'user__first_name', 'user__last_name', 'phone_number'
    )

    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    readonly_fields = ('created', 'modified', 'user', 'profile',)
