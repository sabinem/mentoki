# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_material_unitmaterial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='unitmaterial',
            field=models.ForeignKey(related_name='unitmaterial', blank=True, to='course.CourseMaterialUnit', null=True),
        ),
    ]
