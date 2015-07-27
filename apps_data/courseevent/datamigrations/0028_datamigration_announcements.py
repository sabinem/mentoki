# -*- coding: utf-8 -*-0023_auto_20150617_1038.py

"""
shell script:
from apps_data.courseevent.models import Announcement as NewA
from apps_internal.classroom.models import Announcement as OldA

l = OldA.objects.filter(published=True)

for a in l:
        b = NewA(
            courseevent = a.courseevent,
            title = a.title,
            text = a.text,
            created = a.created,
            modified = a.modified,
            published_at = a.published_at_date,
            published = a.published,
            )
        b.save()

"""


from __future__ import unicode_literals

from django.db import models, migrations

def transfer_material(apps, schema_editor):
    CourseMaterialUnit = apps.get_model("course", "CourseMaterialUnit")
    Lesson = apps.get_model("course", "Lesson")
    Material = apps.get_model("course", "Material")

    for material in CourseMaterialUnit.objects.all():

        material = Material(
            course = material.course,
            title = material.title,
            description = material.description,
            document_type = material.document_type,
            created = material.created,
            modified = material.modified,
            file = material.file,
            slug = material.slug,
            unitmaterial = material
        )
        material.save()

    materials = Material.objects.all()

    for material in materials:
           lesson = Lesson.objects.get(unitmaterial=material.unitmaterial)
           lesson.material.add(material)
           lesson.save()


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0026_datamigration_coursematerial_lesson'),
    ]

    operations = [
        migrations.RunPython(transfer_material)
    ]
