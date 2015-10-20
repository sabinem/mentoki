# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0021_auto_20151018_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(default='25% Einf\xfchrungsrabatt', max_length=200)),
                ('description', froala_editor.fields.FroalaField(default='keine Begr\xfcndung', blank=True)),
                ('new_price', models.DecimalField(null=True, verbose_name='Rabattpreis', max_digits=12, decimal_places=2, blank=True)),
                ('courseproduct', models.ForeignKey(to='mentoki_product.CourseProduct')),
            ],
            options={
                'verbose_name': 'Rabatt',
                'verbose_name_plural': 'Rabatte',
            },
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='discount_text',
            field=models.CharField(default='', max_length=100, blank=True),
        ),
    ]
