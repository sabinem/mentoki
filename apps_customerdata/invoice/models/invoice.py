#encoding: utf-8

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps_customerdata.customer.models.customer import Customer
from apps_customerdata.mentoki_product.models.courseevent import CourseEventProduct



class InvoiceManager(models.Manager):

    def create(self, product, email, payrexx_tld, first_name,
               last_name):
        invoice = Invoice(product=product,
                      amount=product.price_total,
                      currency=product.currency,
                      email=email,
                      payrexx_tld=payrexx_tld,
                      first_name=first_name,
                      last_name=last_name,
                      )
        invoice.save()
        invoice.title = product.courseevent.slug + '-rechnungsnr-' + str(invoice.invoice_nr)
        invoice.save()
        return invoice


class Invoice(models.Model):
    """
    This is an abstract class that defines a structure of Payment model that will be
    generated dynamically with one additional field: ``order``
    """
    # what mentoki wanted
    email = models.EmailField()
    title = models.CharField(max_length=100)
    amount = models.DecimalField(
        _("amount"),
        decimal_places=4,
        max_digits=20)
    currency = models.CharField(
        _("currency"),
        default='EUR',
        max_length=3)
    first_name = models.CharField(max_length=100)
    last_name =models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    product = models.ForeignKey(CourseEventProduct)
    invoice_nr = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    payrexx_tld = models.IntegerField()
    # TODO: monitor paid field!

    objects = InvoiceManager()

    def __unicode__(self):
        return str(self.invoice_nr)





