# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0049_auto_20150410_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseblock',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
    ]
