# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0043_auto_20150327_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseowner',
            name='foto',
            field=models.ImageField(upload_to=apps.course.models.lesson_material_name, blank=True),
            preserve_default=True,
        ),
    ]
