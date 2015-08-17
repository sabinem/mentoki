# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0046_auto_20150817_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='classlesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='lesson.ClassLesson', null=True),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='display_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='courseevent.Forum', null=True),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='homework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='courseevent.Homework', null=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='published',
            field=models.BooleanField(default=False, help_text='Zeigt an, ob das Forum im Klassenzimmer sichtbar ist.', verbose_name='ver\xf6ffentlicht', editable=False),
        ),
        migrations.AlterField(
            model_name='homework',
            name='published',
            field=models.BooleanField(default=False, verbose_name='ver\xf6ffentlichen', editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(related_name='post_author', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='courseevent.Thread', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='thread',
            name='forum',
            field=models.ForeignKey(to='courseevent.Forum', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
