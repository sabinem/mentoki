# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'verbose_name': 'XAnnouncement'},
        ),
        migrations.AlterModelOptions(
            name='classrules',
            options={'verbose_name': 'Xclassrules'},
        ),
        migrations.AlterField(
            model_name='announcement',
            name='courseevent',
            field=models.ForeignKey(related_name='x', to='courseevent.CourseEvent'),
        ),
    ]
