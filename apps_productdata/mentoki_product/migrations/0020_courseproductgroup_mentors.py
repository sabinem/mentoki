# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0019_courseproductgroup_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='mentors',
            field=froala_editor.fields.FroalaField(default='x'),
            preserve_default=False,
        ),
    ]
