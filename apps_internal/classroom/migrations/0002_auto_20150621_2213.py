# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='courseevent',
            field=models.ForeignKey(related_name='kurs', to='courseevent.CourseEvent'),
        ),
        migrations.AlterField(
            model_name='classrules',
            name='courseevent',
            field=models.ForeignKey(related_name='regel', to='courseevent.CourseEvent'),
        ),
    ]
