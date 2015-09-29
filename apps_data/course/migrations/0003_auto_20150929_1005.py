# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseowner',
            options={'verbose_name': 'Kursleitung', 'verbose_name_plural': 'Kursleitungen'},
        ),
    ]
