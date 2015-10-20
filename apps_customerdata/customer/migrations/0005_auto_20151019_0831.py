# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentoki_product', '0021_auto_20151018_2156'),
        ('customer', '0004_auto_20151017_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('order_type', models.CharField(default='Kurs-Teilnahme', max_length=200)),
                ('definitive', models.BooleanField()),
                ('order_status', models.CharField(default='booked', max_length=12, choices=[('booked', 'Gebucht'), ('confirmed', 'Best\xe4tigt')])),
                ('courseproduct', models.ForeignKey(blank=True, to='mentoki_product.CourseProduct', null=True)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='product',
        ),
        migrations.AddField(
            model_name='transaction',
            name='courseproduct',
            field=models.ForeignKey(blank=True, to='mentoki_product.CourseProduct', null=True),
        ),
    ]
