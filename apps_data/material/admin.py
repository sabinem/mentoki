# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.material import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'document_type', 'file')
    list_filter = ('course',)




