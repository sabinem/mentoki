# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0006_auto_20151001_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseeventproduct',
            name='agb',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
