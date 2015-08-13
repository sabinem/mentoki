# -*- coding: utf-8 -*-0023_auto_20150617_1038.py


"""
shell script:
from apps_data.course.models.lesson import Lesson as OldLesson
from apps_data.lesson.models.lesson import Lesson as NewLesson

lessons = OldLesson.objects.filter(level=0)

for l in lessons:
       lesson = NewLesson(title=l.title, text=l.text, description=l.description,
           course=l.course, created=l.created, modified=l.modified, nr=l.nr,
           lesson_nr=l.lesson_nr, old_pk=l.pk)
       p=None
       lesson.insert_at(p)
       lesson.save()

lessons = OldLesson.objects.filter(level=1)

for l in lessons:
       p = NewLesson.objects.get(old_pk=l.parent_id)
       print p


for l in lessons:
       lesson = NewLesson(title=l.title, text=l.text, description=l.description,
           course=l.course, created=l.created, modified=l.modified, nr=l.nr,
           lesson_nr=l.lesson_nr, old_pk=l.pk)
       p = NewLesson.objects.get(old_pk=l.parent_id)
       lesson.insert_at(p)
       lesson.save()

lessons = OldLesson.objects.filter(level=2)

NewLesson.objects.rebuild()
"""


from __future__ import unicode_literals

from django.db import models, migrations

def transfer_material(apps, schema_editor):
    CourseMaterialUnit = apps.get_model("course", "CourseMaterialUnit")
    Lesson = apps.get_model("course", "Lesson")

    for material in CourseMaterialUnit.objects.all():

        parent = Lesson.objects.get(course=material.course, unit=material.unit, unitmaterial=None)

        lesson = Lesson(
            title = material.title,
            text = material.text,
            description = material.description,
            course = material.course,
            created = material.created,
            modified = material.modified,
            nr = material.display_nr,
            unit = material.unit,
            unitmaterial = material
        )
        lesson.insert_at(parent)
        lesson.save()

    Lesson.objects.rebuild()


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0025_datamigration_courseunits'),
    ]

    operations = [
        migrations.RunPython(transfer_material)
    ]
