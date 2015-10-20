# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0018_courseproductgroup_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='about',
            field=froala_editor.fields.FroalaField(default='x'),
            preserve_default=False,
        ),
    ]
