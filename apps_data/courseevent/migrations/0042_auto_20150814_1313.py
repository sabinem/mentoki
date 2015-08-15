# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0041_auto_20150814_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='display_nr',
            field=models.IntegerField(help_text='nicht nach aussen sichtbar', verbose_name='Anzeigereihenfolge'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='text',
            field=models.TextField(help_text='Dieser Text wird den Forumsbeitr\xe4gen vorangestellt und leitet die Kursteilnehmern an, ihre\n                  Beitr\xe4ge zu schreiben.', verbose_name='Ausf\xfchrliche Beschreibung des Forums', blank=True),
        ),
    ]
