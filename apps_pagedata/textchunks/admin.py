# coding: utf-8

"""
Admin for Text chunks
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models import PublicTextChunks


@admin.register(PublicTextChunks)
class PublicTextChunksAdmin(admin.ModelAdmin):
    """
    General Text chunks like Agb, impressum are administerd here
    """
    list_display = ('pagecode', 'meta_keywords', 'meta_description',
                    'meta_title', 'modified' )
    list_filter = ('modified',)

