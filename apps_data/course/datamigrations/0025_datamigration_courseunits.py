# -*- coding: utf-8 -*-0023_auto_20150617_1038.py


"""
shell script:
from apps.course.models import Lesson, CourseUnit

units = CourseUnit.objects.all()

for u in units:
       parent = Lesson.objects.get(course=u.course, block=u.block, unit=None)
       lesson = Lesson(title=u.title, text=u.text, description=u.description,
               course=u.course, created=u.created, modified=u.modified, nr=u.display_nr, unit=u, block=u.block)
       lesson.insert_at(parent)
       lesson.save()

Lesson.objects.rebuild()
"""


from __future__ import unicode_literals

from django.db import models, migrations

def transfer_units(apps, schema_editor):
    CourseUnit = apps.get_model("course", "CourseUnit")
    Lesson = apps.get_model("course", "Lesson")

    for unit in CourseUnit.objects.all():

        parent = Lesson.objects.get(course=unit.course, block=unit.block, unit=None)

        lesson = Lesson(
            title = unit.title,
            text = unit.text,
            description = unit.description,
            course = unit.course,
            created = unit.created,
            modified = unit.modified,
            nr = unit.display_nr,
            unit = unit,
            block = unit.block
        )
        lesson.insert_at(parent)
        lesson.save()

    Lesson.objects.rebuild()


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_datamigration_courseblocks'),
    ]

    operations = [
        migrations.RunPython(transfer_units)
    ]
