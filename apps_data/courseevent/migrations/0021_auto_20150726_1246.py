# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0020_auto_20150725_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseeventlessonpublish',
            options={'verbose_name': 'XLessonPublish'},
        ),
        migrations.AlterModelOptions(
            name='courseeventpubicinformation',
            options={'verbose_name': 'XCourseeventInfo'},
        ),
        migrations.AlterModelOptions(
            name='courseeventunitpublish',
            options={'verbose_name': 'XUnitPublish'},
        ),
        migrations.AddField(
            model_name='thread',
            name='last_author',
            field=models.ForeignKey(related_name='last_post_author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='last_post',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='post_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(related_name='post_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thread',
            name='author',
            field=models.ForeignKey(related_name='thread_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
