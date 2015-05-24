from django.contrib import admin
from .models import *
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

class NewsletterAdmin(MarkdownModelAdmin):
    list_display = ('published_at_date', 'id', 'title',  )
    prepopulated_fields = {'slug': ('title',)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


admin.site.register(Newsletter, NewsletterAdmin)
class NewsletterAdmin(MarkdownModelAdmin):
    list_display = ('published_at_date', 'id', 'title',  )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag)