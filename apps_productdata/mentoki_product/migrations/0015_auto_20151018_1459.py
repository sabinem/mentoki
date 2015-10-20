# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps_productdata.mentoki_product.models.courseproductgroup
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150929_1005'),
        ('mentoki_product', '0014_auto_20151014_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(default='Kurs-Teilnahme', max_length=200)),
                ('description', models.CharField(default='Kurs-Teilnahme', max_length=200, blank=True)),
                ('product_nr', models.CharField(default=1, max_length=20)),
                ('slug', models.SlugField()),
                ('price', models.DecimalField(null=True, verbose_name='Verkaufspreis', max_digits=12, decimal_places=2, blank=True)),
                ('price_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='letzte Preis\xe4nderung am', monitor='price')),
                ('currency', models.CharField(default='EUR', max_length=3, choices=[('EUR', 'Euro'), ('CHF', 'Schweizer Franken')])),
                ('can_be_bought_only_once', models.BooleanField(default=False)),
                ('has_depedencies', models.BooleanField(default=False)),
                ('product_type', models.CharField(default='courseevent', max_length=12, verbose_name='Produktart', choices=[('courseevent', 'Kursteilnahme'), ('part', 'Teilabschnitt einer Kurses'), ('addon', 'anderes Produkt')])),
                ('course', models.ForeignKey(to='course.Course')),
                ('dependencies', models.ForeignKey(blank=True, to='mentoki_product.CourseProduct', null=True)),
            ],
            options={
                'verbose_name': 'Kurs-Produkt',
                'verbose_name_plural': 'Kurs-Produkte',
            },
        ),
        migrations.CreateModel(
            name='CourseProductGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('foto', models.ImageField(help_text='Hier kannst Du ein Foto f\xfcr Deinen Kurs hochladen.', upload_to=apps_productdata.mentoki_product.models.courseproductgroup.foto_location, verbose_name='Foto', blank=True)),
                ('in_one_sentence', models.CharField(help_text='beschreibe den Kurs in einem Satz', max_length=250, verbose_name='in einem Satz')),
                ('course', models.OneToOneField(to='course.Course')),
            ],
            options={
                'verbose_name': 'Kursproduktgruppen',
                'verbose_name_plural': 'Kursproduktgruppen',
            },
        ),
        migrations.DeleteModel(
            name='SimpleProduct',
        ),
        migrations.RemoveField(
            model_name='courseeventproduct',
            name='mentoki_mwst',
        ),
        migrations.RemoveField(
            model_name='courseeventproduct',
            name='mentoki_netto',
        ),
        migrations.RemoveField(
            model_name='courseeventproduct',
            name='mwst',
        ),
        migrations.RemoveField(
            model_name='courseeventproduct',
            name='netto_vk',
        ),
        migrations.RemoveField(
            model_name='courseeventproduct',
            name='price_total',
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='description',
            field=models.CharField(default='Kurs-Teilnahme', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, blank=True, null=True, verbose_name='Verkaufspreis'),
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='price_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='letzte Preis\xe4nderung am', monitor='price'),
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='product_nr',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='slug',
            field=models.SlugField(default='x'),
        ),
        migrations.CreateModel(
            name='CourseAddOnProduct',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('mentoki_product.courseproduct',),
        ),
        migrations.CreateModel(
            name='CourseEventFullProduct',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('mentoki_product.courseproduct',),
        ),
        migrations.CreateModel(
            name='CourseEventPartProduct',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('mentoki_product.courseproduct',),
        ),
    ]
