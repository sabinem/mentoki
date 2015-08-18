# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forum',
            options={'verbose_name': 'XForum'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'XPost'},
        ),
        migrations.AlterModelOptions(
            name='subforum',
            options={'verbose_name': 'XSubForum'},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'verbose_name': 'XThread'},
        ),
        migrations.AlterField(
            model_name='forum',
            name='courseevent',
            field=models.ForeignKey(related_name='kursforum', to='courseevent.CourseEvent'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(related_name='postautor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thread',
            name='author',
            field=models.ForeignKey(related_name='beitragsautor', to=settings.AUTH_USER_MODEL),
        ),
    ]
