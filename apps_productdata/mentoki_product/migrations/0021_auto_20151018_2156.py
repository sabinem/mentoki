# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0016_auto_20150929_1005'),
        ('mentoki_product', '0020_courseproductgroup_mentors'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='courseevent',
            field=models.ForeignKey(blank=True, to='courseevent.CourseEvent', null=True),
        ),
        migrations.AlterField(
            model_name='courseproduct',
            name='description',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
