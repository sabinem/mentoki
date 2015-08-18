# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.material import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    """
    Materials are file that are uploaded and included in the lessons and classlessons
    """
    list_display = ('id', 'title', 'modified', 'created', 'slug', 'document_type', 'file',
                    'um_id')
    list_filter = ('course', 'document_type')




