# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0038_auto_20151029_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseproduct',
            options={'verbose_name': 'Kurs', 'verbose_name_plural': 'Kurs'},
        ),
        migrations.AlterModelOptions(
            name='courseproductpart',
            options={'verbose_name': 'Kursabschnitt', 'verbose_name_plural': 'Kursabschnitt'},
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='dependencies',
            field=models.ForeignKey(related_name='dependent_on', blank=True, to='mentoki_product.CourseProduct', null=True),
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='part_of',
            field=models.ForeignKey(related_name='belongs_to', blank=True, to='mentoki_product.CourseProduct', null=True),
        ),
    ]
