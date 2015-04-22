# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0022_auto_20150413_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.SlugField(unique=True)),
                ('text', models.TextField(blank=True)),
                ('contacttype', models.CharField(default='0', max_length=2, choices=[('0', 'Allgemein'), ('1', 'Lehrer'), ('2', 'Sch\xfcler')])),
                ('courseevent', models.ForeignKey(blank=True, to='courseevent.CourseEvent', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
