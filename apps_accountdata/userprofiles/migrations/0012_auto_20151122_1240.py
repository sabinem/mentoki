# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0011_auto_20151117_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorsprofile',
            name='meta_description_mentors',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='mentorsprofile',
            name='meta_keywords_mentors',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='mentorsprofile',
            name='meta_title_mentors',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Titel'),
        ),
    ]
