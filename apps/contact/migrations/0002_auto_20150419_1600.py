# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='text',
            new_name='message',
        ),
        migrations.AddField(
            model_name='contact',
            name='persondescription',
            field=models.CharField(max_length=100, verbose_name='zu Deiner Person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='projectdescription',
            field=models.CharField(max_length=100, verbose_name='Kursbeschreibung', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='projecttype',
            field=models.CharField(max_length=100, verbose_name='Kurstitel', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacttype',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'Allgemein'), ('1', 'Starterkurs'), ('2', 'Kursvorbuchung')]),
            preserve_default=True,
        ),
    ]
