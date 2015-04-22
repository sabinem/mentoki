# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0050_auto_20150410_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseblock',
            name='display_nr',
            field=models.IntegerField(verbose_name='Lektions-Nummer, steuert die Anzeigereihenfolge bei unnumerierten Unterrichtsbl\xf6cken'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='Lektions-Nummer, steuert die Anzeigereihenfolge bei unnumerierten Unterrichtsbl\xf6cken'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='Lektions-Nummer, steuert die Anzeigereihenfolge bei unnumerierten Unterrichtsbl\xf6cken'),
            preserve_default=True,
        ),
    ]
