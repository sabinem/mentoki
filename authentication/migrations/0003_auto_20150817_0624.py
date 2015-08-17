# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_account_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_student',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_teacher',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
