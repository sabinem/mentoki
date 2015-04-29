# import from django
from django.contrib import admin
# import from own app
from .models import Course, CourseBlock, CourseUnit, CourseMaterialUnit, CourseOwner


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'email', 'modified', 'status')


@admin.register(CourseOwner)
class CourseOwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'user', 'modified', 'status')


@admin.register(CourseBlock)
class CourseBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'is_numbered', 'status')
    list_filter = ('course',)
    list_display_links = ('title',)


@admin.register(CourseUnit)
class CourseUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'block', 'title', 'unit_nr', 'status')
    list_filter = ('course', 'block')
    list_display_links = ('title',)


@admin.register(CourseMaterialUnit)
class CourseMaterialUnitAdmin(admin.ModelAdmin):
    list_display = ('file', 'slug', 'id', 'course', 'unit', 'title', 'document_type', 'status' )
    list_filter = ('course', 'document_type')


