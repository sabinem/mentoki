# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0016_auto_20150929_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEventProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('pricemodel', models.CharField(default='0', max_length=2, verbose_name='interner Status', choices=[('0', 'regul\xe4r'), ('1', 'Gutscheine'), ('a', 'Empfehlung')])),
                ('price', models.DecimalField(null=True, verbose_name='Preis', max_digits=12, decimal_places=2, blank=True)),
                ('in_one_sentence', models.CharField(max_length=250, verbose_name='in einem Satz')),
                ('courseevent', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='courseevent.CourseEvent')),
            ],
            options={
                'verbose_name': 'Kursereignisverkauf',
                'verbose_name_plural': 'Kursereignisverk\xe4ufe',
            },
        ),
    ]
