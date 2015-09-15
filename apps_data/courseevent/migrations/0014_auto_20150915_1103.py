# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0013_auto_20150905_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='published',
            field=models.BooleanField(default=False, help_text='Beim Ver\xf6ffentlichen wird die Ank\xfcndigung an alle Kursteilnehmer\n        und Mentoren verschickt:\n        ', verbose_name='ver\xf6ffentlichen?'),
        ),
        migrations.AlterField(
            model_name='studentswork',
            name='homework',
            field=models.ForeignKey(verbose_name='Aufgabe', to='lesson.ClassLesson'),
        ),
    ]
