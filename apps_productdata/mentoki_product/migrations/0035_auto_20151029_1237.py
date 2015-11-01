# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150929_1005'),
        ('courseevent', '0016_auto_20150929_1005'),
        ('mentoki_product', '0034_courseproduct_descriptor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(default='Kurs-Teilnahme', max_length=200)),
                ('description', froala_editor.fields.FroalaField()),
                ('descriptor', models.CharField(default='x', max_length=250)),
                ('price', models.DecimalField(null=True, verbose_name='Verkaufspreis', max_digits=12, decimal_places=2, blank=True)),
                ('currency', models.CharField(default=b'EUR', max_length=3, choices=[(b'EUR', 'Euro'), (b'CHF', 'Schweizer Franken')])),
                ('price_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='letzte Preis\xe4nderung am', monitor='price')),
                ('slug', models.SlugField()),
                ('display_nr', models.IntegerField(default=1)),
                ('meta_keywords', models.CharField(default='x', max_length=200)),
                ('meta_description', models.CharField(default='x', max_length=200)),
                ('meta_title', models.CharField(default='x', max_length=100)),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkte',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='Kurs', max_length=200)),
                ('description', models.TextField()),
                ('is_courseevent', models.BooleanField()),
                ('is_courseevent_part', models.BooleanField()),
                ('is_test', models.BooleanField()),
                ('belongs_to_course', models.BooleanField()),
                ('can_be_bought_only_once', models.BooleanField(default=False)),
                ('has_dependencies', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='course.Course')),
                ('courseevent', models.ForeignKey(blank=True, to='courseevent.CourseEvent', null=True)),
                ('dependencies', models.ForeignKey(blank=True, to='mentoki_product.ProductType', null=True)),
            ],
            options={
                'verbose_name': 'Produktart',
                'verbose_name_plural': 'Produktarten',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(verbose_name='Produktart', to='mentoki_product.ProductType'),
        ),
    ]
