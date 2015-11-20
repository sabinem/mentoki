# coding: utf-8

"""
Admin for Text chunks
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models import StaticPublicPages


@admin.register(StaticPublicPages)
class PublicPagesAdmin(admin.ModelAdmin):
    """
    General Text chunks like Agb, impressum are administerd here
    """
    list_display = ('pagecode', 'slug', 'title',
                    'meta_title', 'modified' )
    list_filter = ('modified',)

