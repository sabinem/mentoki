# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_temporder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporder',
            name='participant_email',
            field=models.EmailField(max_length=254, verbose_name='Email des Teilnehmers', blank=True),
        ),
    ]
