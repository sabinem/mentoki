# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0023_auto_20160119_2041'),
        ('lesson', '0011_auto_20160120_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('text', models.TextField(verbose_name='Text')),
                ('author', models.ForeignKey(related_name='question_author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('classlessonstep', models.ForeignKey(related_name='question_to_lesson', to='lesson.ClassLesson')),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
            ],
            options={
                'verbose_name': 'Kommentar',
                'verbose_name_plural': 'Kommentare',
            },
        ),
    ]
