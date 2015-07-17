# -*- coding: utf-8 -*-0023_auto_20150617_1038.py


"""
shell script:
from apps.course.models import Lesson, CourseMaterialUnit, Material

materials = CourseMaterialUnit.objects.exclude(file="")

for m in materials:
        material = Material(
            course = m.course,
            title = m.title,
            description = m.description,
            document_type = m.document_type,
            created = m.created,
            modified = m.modified,
            unitmaterial = m,
            file = m.file,
            slug = m.slug
            )

        material.save()

Lesson.objects.rebuild()

materials = Material.objects.all()

for m in materials:
       l = Lesson.objects.get(unitmaterial=m.unitmaterial)
       l.material.add(m)
       l.save()

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
