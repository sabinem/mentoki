# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_courseowner_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseowner',
            name='text',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
