# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_auto_20151021_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_valid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_type',
        ),
        migrations.RemoveField(
            model_name='order',
            name='participant_email',
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='Teilnehmer, der teilnimmt'),
        ),
    ]
