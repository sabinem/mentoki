# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0031_auto_20151022_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseeventproduct',
            name='courseevent',
        ),
        migrations.DeleteModel(
            name='CourseEventProduct',
        ),
    ]
