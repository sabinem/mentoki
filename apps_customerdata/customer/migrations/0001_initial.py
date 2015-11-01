# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import model_utils.fields
import django.utils.timezone
from django.conf import settings
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0003_auto_20150929_1005'),
        ('mentoki_product', '0033_auto_20151023_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('braintree_customer_id', models.CharField(max_length=36, verbose_name='braintree_customer_id', blank=True)),
                ('user', models.OneToOneField(related_name='customer', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kunde',
                'verbose_name_plural': 'Kunden',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('email', models.EmailField(default='x', max_length=254, verbose_name='Email des Teilnehmers')),
                ('first_name', models.CharField(default='x', max_length=40, verbose_name='Vorname der Teilnehmers')),
                ('last_name', models.CharField(default='x', max_length=40)),
                ('username', models.CharField(max_length=40, blank=True)),
                ('street_line_1', models.CharField(max_length=100, blank=True)),
                ('street_line_2', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=100, blank=True)),
                ('postal_code', models.CharField(max_length=20, blank=True)),
                ('postal_box', models.CharField(max_length=20, verbose_name='Postal box', blank=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('phone_nr', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
                ('order_status', models.CharField(default='initial', max_length=12, choices=[('initial', 'aufgenommen'), ('paid', 'bezahlt'), ('canceled', 'storniert'), ('refunded', 'zur\xfcckerstattet')])),
                ('amount', models.DecimalField(default=0, verbose_name='Betrag', max_digits=20, decimal_places=4)),
                ('currency', models.CharField(default=b'EUR', max_length=3, choices=[(b'EUR', 'Euro'), (b'CHF', 'Schweizer Franken')])),
                ('course', models.ForeignKey(blank=True, to='course.Course', null=True)),
                ('courseproduct', models.ForeignKey(blank=True, to='mentoki_product.CourseProduct', null=True)),
                ('customer', models.ForeignKey(related_name='Kunde', verbose_name='Kunde, Teilnehmer, der gebucht hat', blank=True, to='customer.Customer', null=True)),
            ],
            options={
                'verbose_name': 'Buchung',
                'verbose_name_plural': 'Buchungen',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('braintree_transaction_id', models.CharField(max_length=50, blank=True)),
                ('braintree_merchant_account_id', models.CharField(max_length=100, verbose_name=b'braintree_merchant', blank=True)),
                ('braintree_customer_id', models.CharField(max_length=100, verbose_name=b'braintree Kundennr.', blank=True)),
                ('amount', models.DecimalField(verbose_name='amount', max_digits=20, decimal_places=4)),
                ('currency', models.CharField(default=b'EUR', max_length=3, choices=[(b'EUR', 'Euro'), (b'CHF', 'Schweizer Franken')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('flag_sucess', models.BooleanField(default=False)),
                ('course', models.ForeignKey(blank=True, to='course.Course', null=True)),
                ('customer', models.ForeignKey(blank=True, to='customer.Customer', null=True)),
                ('order', models.ForeignKey(to='customer.Order')),
            ],
            options={
                'verbose_name': 'Transaktion',
                'verbose_name_plural': 'Transaktionen',
            },
        ),
    ]
