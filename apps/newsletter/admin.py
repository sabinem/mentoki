from django.contrib import admin
from .models import *
# import from django
from django.contrib import admin
# import from own app
from .models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('published_at_date', 'id', 'title',  )

