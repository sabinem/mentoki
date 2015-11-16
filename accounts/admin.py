# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User as MentokiUser
from django.contrib.auth.admin import UserAdmin


class MentokiUserAdmin(UserAdmin):
    """
    Adminstration of Users
    """
    model = MentokiUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('id', 'username', 'email', 'checkout_product_pk', 'is_staff', 'is_superuser', 'is_teacher', 'is_student', 'studying')
    list_filter = ('is_superuser', 'is_teacher', 'is_student')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'profile_image'
                           )}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(MentokiUser, MentokiUserAdmin)