# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0016_auto_20150929_1005'),
        ('mentoki_product', '0039_auto_20151029_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='courseevent',
            field=models.ForeignKey(blank=True, to='courseevent.CourseEvent', null=True),
        ),
    ]
