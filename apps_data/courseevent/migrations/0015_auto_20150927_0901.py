# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0014_auto_20150926_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='text',
            field=froala_editor.fields.FroalaField(verbose_name='Text'),
        ),
    ]
