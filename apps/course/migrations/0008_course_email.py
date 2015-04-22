# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20141217_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='email',
            field=models.EmailField(default=b'info@netteachers.de', max_length=75),
            preserve_default=True,
        ),
    ]
