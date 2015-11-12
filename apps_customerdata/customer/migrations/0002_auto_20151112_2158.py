# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='error_code',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='error_message',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='flag_payment_sucess',
        ),
        migrations.AddField(
            model_name='transaction',
            name='braintree_error_message',
            field=models.CharField(max_length=250, verbose_name='aus braintree Fehlernachricht: besetzt im Fehlerfall ', blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='braintree_processor_response_code',
            field=models.CharField(max_length=4, verbose_name='Banken Processor Code: besetzt im Fehlerfall ', blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='braintree_processor_response_text',
            field=models.CharField(max_length=250, verbose_name='Banken Processor Text: besetzt im Fehlerfall ', blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='success',
            field=models.BooleanField(default=False, verbose_name='Flag ob die Transaktion erfolgreich war, insofern als tats\xe4chlich bezahlt wurde.'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(verbose_name='Betrag', max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_amount',
            field=models.CharField(help_text='Was braintree abgebucht hat', max_length=10, verbose_name='braintree Betrag', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_error_details',
            field=models.TextField(verbose_name='aus braintree deep errors: besetzt im Fehlerfall ', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_merchant_account_id',
            field=models.CharField(max_length=20, verbose_name='braintree Merchant Accountnr.', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_payment_token',
            field=models.CharField(max_length=10, verbose_name='braintree Zahlunsmittel-Token.', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_transaction_id',
            field=models.CharField(max_length=10, verbose_name='braintree Transaktionsnr.', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='course',
            field=models.ForeignKey(verbose_name='Kurs', blank=True, to='course.Course', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(verbose_name='Kunde', blank=True, to='customer.Customer', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email des Teilnehmers', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='first_name',
            field=models.CharField(max_length=40, verbose_name='Vorname der Teilnehmers', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='Nachname der Teilnehmers', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='order',
            field=models.ForeignKey(verbose_name='Auftrag', to='customer.Order'),
        ),
    ]
