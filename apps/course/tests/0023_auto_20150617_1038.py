# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def transfer_blocks(apps, schema_editor):
    CourseBlock = apps.get_model("course", "CourseBlock")
    Lesson = apps.get_model("course", "Lesson")

    for block in CourseBlock.objects.all():
        lesson = Lesson(
            title = block.title,
            text = block.text,
            description = block.description,
            course = block.course,
            created = block.created,
            modified = block.modified
        )
        lesson.save()


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_auto_20150617_1107'),
    ]

    operations = [
        migrations.RunPython(transfer_blocks)
    ]
