# -*- coding: utf-8 -*-0023_auto_20150617_1038.py


"""
shell script:
from apps.course.models import Lesson, CourseUnit, CourseMaterialUnit

materials = CourseMaterialUnit.objects.all()

for m in materials:
       try:
           parent = Lesson.objects.get(course=m.course, unit=m.unit, unitmaterial=None)
       except:
           parent = None

       lesson = Lesson(title=m.title, text=m.text, description=m.description,
           course=m.course, created=m.created, modified=m.modified, nr=m.display_nr, unit=m.unit, unitmaterial=m)
       lesson.insert_at(parent)
       lesson.save()

Lesson.objects.rebuild()
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
