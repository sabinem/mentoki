# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0007_auto_20150709_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='participation',
            field=models.ManyToManyField(related_name='participation', through='courseevent.CourseEventParticipation', to=settings.AUTH_USER_MODEL),
        ),
    ]
