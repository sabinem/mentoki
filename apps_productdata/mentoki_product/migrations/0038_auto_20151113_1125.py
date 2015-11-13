# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150929_1005'),
        ('mentoki_product', '0037_auto_20151112_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseProductSubGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=250)),
                ('course', models.ForeignKey(to='course.Course')),
            ],
            options={
                'verbose_name': 'Kursproduktuntergruppe',
                'verbose_name_plural': 'Kursproduktuntergruppen',
            },
        ),
        migrations.AlterModelOptions(
            name='courseproductgroup',
            options={'verbose_name': 'Kursproduktgruppe', 'verbose_name_plural': 'Kursproduktgruppen'},
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='courseproductgroup',
            field=models.ForeignKey(default=1, to='mentoki_product.CourseProductGroup'),
        ),
        migrations.AddField(
            model_name='courseproductsubgroup',
            name='courseproductgroup',
            field=models.ForeignKey(default=1, to='mentoki_product.CourseProductGroup'),
        ),
    ]
