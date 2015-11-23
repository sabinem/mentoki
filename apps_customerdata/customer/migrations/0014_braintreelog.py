# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_auto_20151122_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='BraintreeLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('input', models.TextField()),
                ('result', models.TextField()),
                ('transaction', models.ForeignKey(to='customer.Transaction')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
