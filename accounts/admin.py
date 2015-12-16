# coding: utf-8

"""
Admin for Custom User Model
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

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

    list_display = ('id', 'username', 'email', 'checkout_product_pk', 'is_staff', 'is_superuser', 'is_lektor', 'is_teacher', 'is_student', 'studying')
    list_filter = ('is_superuser', 'is_teacher', 'is_student',  'is_staff',  'is_lektor',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'is_teacher',
                           'is_female', 'is_lektor',
                           'last_name', 'profile_image'
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