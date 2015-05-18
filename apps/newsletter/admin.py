from django.contrib import admin
from .models import *
from django_markdown.admin import MarkdownModelAdmin


class NewsletterAdmin(MarkdownModelAdmin):
    list_display = ('published_at_date', 'id', 'title',  )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Newsletter, NewsletterAdmin)
class NewsletterAdmin(MarkdownModelAdmin):
    list_display = ('published_at_date', 'id', 'title',  )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag)