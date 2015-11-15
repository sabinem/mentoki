# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0009_mentorsprofile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorsprofile',
            name='text',
            field=froala_editor.fields.FroalaField(verbose_name='ausf\xfchrliche Beschreibung', blank=True),
        ),
    ]
