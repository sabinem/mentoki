# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20150420_0759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='projecttype',
            new_name='projecttitle',
        ),
        migrations.AlterField(
            model_name='contact',
            name='courseevent',
            field=models.ForeignKey(verbose_name='Welcher Kurs interessiert Dich?', blank=True, to='courseevent.CourseEvent', null=True),
            preserve_default=True,
        ),
    ]
