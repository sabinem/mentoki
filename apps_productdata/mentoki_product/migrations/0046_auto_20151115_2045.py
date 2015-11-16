# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0045_auto_20151114_1447'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courseproduct',
            unique_together=set([('courseevent', 'name')]),
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='meta_title',
        ),
    ]
