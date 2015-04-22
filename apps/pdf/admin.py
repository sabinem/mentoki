# import from django
from django.contrib import admin
# import from own app
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file','slug' )


admin.site.register(Document, DocumentAdmin)