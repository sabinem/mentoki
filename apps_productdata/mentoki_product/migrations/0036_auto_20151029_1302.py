# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0035_auto_20151029_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_type',
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
        migrations.RenameField(
            model_name='courseproduct',
            old_name='descriptor',
            new_name='invoice_descriptor',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='can_be_bought_only_once',
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
        migrations.RemoveField(
            model_name='producttype',
            name='course',
        ),
        migrations.RemoveField(
            model_name='producttype',
            name='courseevent',
        ),
        migrations.RemoveField(
            model_name='producttype',
            name='dependencies',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
