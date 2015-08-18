# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0060_auto_20150724_1132'),
        ('courseevent', '0012_menu_item_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassroomMenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('item_type', models.CharField(max_length=15, choices=[('forum', 'forum'), ('lesson', 'lesson or lesson block'), ('anouncements', 'announcements'), ('homework', 'homework'), ('last_posts', 'latest forum posts')])),
                ('display_nr', models.IntegerField()),
                ('display_title', models.CharField(default='x', max_length=200)),
                ('published', models.BooleanField(default=False)),
                ('published_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), monitor='published')),
                ('is_start_item', models.BooleanField()),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('forum', models.ForeignKey(blank=True, to='courseevent.Forum', null=True)),
                ('homework', models.ForeignKey(blank=True, to='courseevent.Homework', null=True)),
                ('lesson', models.ForeignKey(blank=True, to='course.Lesson', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='menu',
            name='courseevent',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='forum',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='homework',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='lesson',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
