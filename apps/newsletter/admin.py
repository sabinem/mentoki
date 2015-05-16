from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('published_at_date', 'id', 'title',  )


admin.site.register(Newsletter, NewsletterAdmin)