# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0054_auto_20150424_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='fileslug',
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Anzeigen bei der Kursausschreibung?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='display_nr',
            field=models.IntegerField(default=1, verbose_name='Anzeigereihenfolge bei mehreren Kursleitern'),
            preserve_default=True,
        ),
    ]
