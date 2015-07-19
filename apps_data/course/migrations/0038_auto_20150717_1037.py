# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0037_auto_20150715_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(related_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='author',
            field=models.ForeignKey(default='1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
