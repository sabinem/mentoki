# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150929_1005'),
        ('mentoki_product', '0053_auto_20151204_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseProductGroupField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=200)),
                ('text', froala_editor.fields.FroalaField()),
                ('pagemark', models.CharField(max_length=200)),
                ('display_nr', models.IntegerField()),
                ('course', models.OneToOneField(to='course.Course')),
                ('courseproductgroup', models.ForeignKey(to='mentoki_product.CourseProductGroup')),
            ],
            options={
                'verbose_name': 'Kursproduktgruppefeld',
                'verbose_name_plural': 'Kursproduktgruppenfelder',
            },
        ),
    ]
