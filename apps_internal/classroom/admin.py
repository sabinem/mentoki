from django.contrib import admin
from .models import Announcement, ClassRules


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('published_at_date', 'courseevent', 'id', 'title',  )


class ClassRulesAdmin(admin.ModelAdmin):
    list_display = ('created', 'courseevent', 'id', 'title', 'status')


admin.site.register(ClassRules, ClassRulesAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
