# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20150419_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contactinfo',
            field=models.TextField(verbose_name='Wie k\xf6nnen wir Dich erreichen?', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Deine Nachricht', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='projectdescription',
            field=models.TextField(verbose_name='Beschreibe Dein Kursprojekt', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='projecttype',
            field=models.CharField(max_length=100, verbose_name='Titel f\xfcr Dein Kursprojekt', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='qualification',
            field=models.TextField(verbose_name='Was qualifiziert Dich daf\xfcr?', blank=True),
            preserve_default=True,
        ),
    ]
