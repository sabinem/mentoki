# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150929_1005'),
        ('mentoki_product', '0039_courseproduct_courseproductsubgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseProductPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(default='Kurs-Teilnahme', max_length=200)),
                ('description', froala_editor.fields.FroalaField()),
                ('price', models.DecimalField(null=True, verbose_name='Verkaufspreis', max_digits=12, decimal_places=2, blank=True)),
                ('currency', models.IntegerField(default=1)),
                ('price_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='letzte Preis\xe4nderung am', monitor='price')),
                ('slug', models.SlugField()),
                ('display_nr', models.IntegerField(default=1)),
                ('meta_keywords', models.CharField(default='x', max_length=200)),
                ('meta_description', models.CharField(default='x', max_length=200)),
                ('meta_title', models.CharField(default='x', max_length=100)),
                ('product_type', models.IntegerField(default=20)),
                ('part_nr', models.IntegerField()),
                ('course', models.ForeignKey(to='course.Course')),
            ],
            options={
                'verbose_name': 'Kursproduktabschnitt',
                'verbose_name_plural': 'Kursproduktabschnitte',
            },
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='can_be_bought_in_parts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courseproductpart',
            name='courseproduct',
            field=models.ForeignKey(default=1, to='mentoki_product.CourseProduct'),
        ),
    ]
