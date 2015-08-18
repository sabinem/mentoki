# -*- coding: utf-8 -*-0023_auto_20150617_1038.py


"""
shell script:
from apps.course.models import CourseBlock, Lesson

blocks = CourseBlock.objects.all()

for b in blocks:
...    lesson = Lesson(title=b.title, text=b.text, description=b.description,
...        course= b.course, created=b.created, modified=b.modified, block=b)
...    lesson.insert_at(None)
...    lesson.save()

Lesson.objects.rebuild()
"""


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
            modified = block.modified,
            block = block
        )
        lesson.insert_at(None)
        lesson.save()

    Lesson.objects.rebuild()


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_auto_20150617_1449'),
    ]

    operations = [
        migrations.RunPython(transfer_blocks)
    ]
