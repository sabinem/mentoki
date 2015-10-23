# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_auto_20151022_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporder',
            name='user',
            field=models.ForeignKey(verbose_name='Teilnehmer als Benutzer', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
