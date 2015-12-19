# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0016_auto_20151216_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorsprofile',
            name='at_mentoki',
            field=froala_editor.fields.FroalaField(verbose_name='Rolle bei Mentoki', blank=True),
        ),
    ]
