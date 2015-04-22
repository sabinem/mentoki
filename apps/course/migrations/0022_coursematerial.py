# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '__first__'),
        ('course', '0021_auto_20150124_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name=b'Ueberschrift')),
                ('text', models.TextField(blank=True)),
                ('display_nr', models.IntegerField()),
                ('menu_item', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='course.Course')),
                ('document', models.ForeignKey(default=1, to='pdf.Document')),
                ('unit', models.ForeignKey(to='course.CourseUnit')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
