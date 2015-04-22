# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0048_courseblock_show_full'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseblock',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge', validators=[apps.course.models.validate_unique]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge', validators=[apps.course.models.validate_unique]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge', validators=[apps.course.models.validate_unique]),
            preserve_default=True,
        ),
    ]
