# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0052_auto_20151122_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_description_description',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_description_mentors',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_description_offers',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_keywords_description',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_keywords_mentors',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_keywords_offers',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_title_description',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_title_mentors',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_title_offers',
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='video',
            field=models.TextField(verbose_name='Video', blank=True),
        ),
    ]
