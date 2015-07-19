# -*- coding: utf-8 -*-0023_auto_20150617_1038.py


"""
shell script:
from apps_data.course.models import Lesson, Material, Course

course = Course.objects.all()

a = dict()

for c in course:
    a[c.id] = c.author

print a


materials = Material.objects.all()

for m in materials:
        m.author = a[m.course_id]
        m.save()

lessons = Lesson.objects.all()

for l in lessons:
        l.author = a[l.course_id]
        l.save()

"""
