# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
import apps.course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0039_auto_20150323_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name=b'Ueberschrift')),
                ('text', models.TextField(blank=True)),
                ('display_nr', models.IntegerField()),
                ('is_numbered', models.BooleanField(default=True)),
                ('course', models.ForeignKey(to='course.Course')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='sub_unit_nr',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='block',
            field=models.ForeignKey(blank=True, to='course.CourseBlock', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='unit_nr',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.lesson_material_name, blank=True),
            preserve_default=True,
        ),
    ]
