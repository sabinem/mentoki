# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0040_specialoffer_courseevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialoffer',
            name='courseevent',
        ),
        migrations.RemoveField(
            model_name='specialoffer',
            name='courseproduct',
        ),
        migrations.RemoveField(
            model_name='specialoffer',
            name='vaild_for',
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='course',
            field=models.OneToOneField(null=True, blank=True, to='course.Course'),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='description',
            field=froala_editor.fields.FroalaField(default='zur Einf\xfchrung', blank=True),
        ),
    ]
