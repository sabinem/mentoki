# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_auto_20150916_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlesson',
            name='icon',
            field=fontawesome.fields.IconField(help_text='Neben dem Men\xfceintrag kann ein Icon angezeigt werden.', max_length=60, verbose_name='Icon', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='icon',
            field=fontawesome.fields.IconField(help_text='Neben dem Men\xfceintrag kann ein Icon angezeigt werden.', max_length=60, verbose_name='Icon', blank=True),
        ),
    ]
