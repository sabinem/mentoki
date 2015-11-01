# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0017_courseeventparticipation_participation_type'),
        ('mentoki_product', '0033_auto_20151023_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='Kurs', max_length=200)),
                ('description', models.TextField()),
                ('is_part', models.BooleanField()),
                ('is_test', models.BooleanField()),
                ('belongs_to_course', models.BooleanField()),
                ('is_courseevent_participation', models.BooleanField()),
                ('can_be_bought_only_once', models.BooleanField(default=False)),
                ('has_dependencies', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Produktart',
                'verbose_name_plural': 'Produktarten',
            },
        ),
        migrations.DeleteModel(
            name='CourseAddOnProduct',
        ),
        migrations.DeleteModel(
            name='CourseEventFullProduct',
        ),
        migrations.DeleteModel(
            name='CourseEventPartProduct',
        ),
        migrations.AlterModelOptions(
            name='courseproduct',
            options={'verbose_name': 'Kursangebote', 'verbose_name_plural': 'Kursangebote'},
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='can_be_bought_only_once',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='dependencies',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='has_dependencies',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='product_nr',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='product_type',
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='dependency',
            field=models.ForeignKey(related_name='dependent_on', blank=True, to='mentoki_product.CourseProduct', null=True),
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='invoice_descriptor',
            field=models.CharField(default='x', max_length=250),
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='part_of',
            field=models.ForeignKey(related_name='belongs_to', blank=True, to='mentoki_product.CourseProduct', null=True),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='courseevent',
            field=models.ForeignKey(blank=True, to='courseevent.CourseEvent', null=True),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='reach',
            field=models.CharField(default=b'course', max_length=10, choices=[(b'course', 'course'), (b'courseevent', 'courseevent'), (b'product', 'product')]),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='description',
            field=froala_editor.fields.FroalaField(default='zur Einf\xfchrung', blank=True),
        ),
    ]
