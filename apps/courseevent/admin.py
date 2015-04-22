# import from django
from django.contrib import admin
# import from this apps
from .models import CourseEvent, CourseeventUnitPublish, CourseEventParticipation, \
    CourseEventPubicInformation



@admin.register(CourseEvent)
class CourseEventAdmin(admin.ModelAdmin):
    list_display = ('slug', 'id', 'title', 'course', )
    list_filter =  ('course',)


@admin.register(CourseeventUnitPublish)
class CourseeventUnitPublishAdmin(admin.ModelAdmin):
    list_display = ('unit', 'courseevent')
    list_filter = ('unit', 'courseevent')


@admin.register(CourseEventParticipation)
class CourseEventParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'courseevent')
    list_filter = ('user', 'courseevent')


@admin.register(CourseEventPubicInformation)
class CourseEventPubicInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'courseevent',)
    list_filter = ('courseevent',)