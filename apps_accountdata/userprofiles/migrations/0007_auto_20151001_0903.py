# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0006_auto_20151001_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorsprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Mentor', to=settings.AUTH_USER_MODEL),
        ),
    ]
