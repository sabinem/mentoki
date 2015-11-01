# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_unfinished_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='unfinished_purchase',
        ),
        migrations.AddField(
            model_name='transaction',
            name='email',
            field=models.EmailField(default=b'x', max_length=254, verbose_name='Email des Teilnehmers'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='first_name',
            field=models.CharField(default=b'x', max_length=40, verbose_name='Vorname der Teilnehmers'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='last_name',
            field=models.CharField(default=b'x', max_length=40),
        ),
        migrations.AddField(
            model_name='transaction',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set([('customer', 'courseproduct')]),
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),

        migrations.RemoveField(
            model_name='order',
            name='postal_box',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_line_1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_line_2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='username',
        ),
    ]
