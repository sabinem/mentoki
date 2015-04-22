# import from django
from django.contrib import admin
# import from own app
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_contacttype_display', 'email')