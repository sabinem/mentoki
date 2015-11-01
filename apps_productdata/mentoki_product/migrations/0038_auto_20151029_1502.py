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
        ('mentoki_product', '0037_courseproduct_product_type'),
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
                ('invoice_descriptor', models.CharField(default='x', max_length=250)),
                ('price', models.DecimalField(null=True, verbose_name='Verkaufspreis', max_digits=12, decimal_places=2, blank=True)),
                ('currency', models.CharField(default=b'EUR', max_length=3, choices=[(b'EUR', 'Euro'), (b'CHF', 'Schweizer Franken')])),
                ('price_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='letzte Preis\xe4nderung am', monitor='price')),
                ('slug', models.SlugField()),
                ('display_nr', models.IntegerField(default=1)),
                ('meta_keywords', models.CharField(default='x', max_length=200)),
                ('meta_description', models.CharField(default='x', max_length=200)),
                ('meta_title', models.CharField(default='x', max_length=100)),
                ('course', models.ForeignKey(to='course.Course')),
                ('courseevent', models.ForeignKey(blank=True, to='courseevent.CourseEvent', null=True)),
                ('dependencies', models.ForeignKey(blank=True, to='mentoki_product.CourseProductPart', null=True)),
                ('product_type', models.ForeignKey(verbose_name='Produktart', to='mentoki_product.ProductType')),
            ],
            options={
                'verbose_name': 'Kurs-Produkt',
                'verbose_name_plural': 'Kurs-Produkte',
            },
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='dependencies',
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='vaild_for',
            field=models.CharField(default=b'course', max_length=10, choices=[(b'course', 'course'), (b'courseevent', 'courseevent'), (b'product', 'product')]),
        ),
    ]
