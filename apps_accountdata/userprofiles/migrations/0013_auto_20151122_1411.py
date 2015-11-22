# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0012_auto_20151122_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorsprofile',
            name='meta_description_mentors',
            field=models.CharField(default='Mentoki', max_length=250, verbose_name='Meta Description'),
        ),
        migrations.AlterField(
            model_name='mentorsprofile',
            name='meta_keywords_mentors',
            field=models.CharField(default='Mentoki', max_length=250, verbose_name='Meta Keywords'),
        ),
        migrations.AlterField(
            model_name='mentorsprofile',
            name='meta_title_mentors',
            field=models.CharField(default='Mentoki', max_length=250, verbose_name='Meta Titel'),
        ),
    ]
