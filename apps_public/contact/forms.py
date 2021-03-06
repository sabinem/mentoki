# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from django.template.loader import get_template
from django.template import Context
from django.conf import settings

from mailqueue.models import MailerMessage


class ContactForm(forms.Form):
    """
    Contact Form
    """

    name = forms.CharField(
        required=True,
        max_length=100,
        label='Ihr Name',
        widget=forms.TextInput(
           attrs={'placeholder':
                  'Name',
                  'autofocus': 'autofocus'}))
    email = forms.EmailField(
        required=True,
        max_length=100,
        label='Ihre Email',
        widget=forms.TextInput(
           attrs={'placeholder':
                  'Email'}))
    message = forms.CharField(
        required=True,
        label='Ihre Nachricht',
        widget=forms.Textarea(
            attrs={'placeholder':
                  'Nachricht'}))

    OUTGOING=u'Kontakt: Bestätigungsmail an den Kunden'
    INTERNAL=u'Weiterleitung Kontaktanfrage, bitte beantworten!'
    CONTACT_EMAIL=settings.MENTOKI_INFO_EMAIL

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    def send_email_visitor(self):
        # send email to requesting email
        # this method is called with cleaned from data
        subject = "Ihre Nachricht an mentoki"
        to = [self.cleaned_data['email']]
        from_mail = 'mentoki@mentoki.com'

        # prepare template
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
            'betreff': "Ihre Nachricht",
        }
        message = get_template('email/contact/to_customer.html').render(Context(context))
        to_customer = MailerMessage()
        to_customer.subject = "Ihre Nachricht an mentoki"
        to_customer.to_address = self.cleaned_data['email']
        to_customer.from_address = ContactForm.CONTACT_EMAIL
        to_customer.content = ContactForm.OUTGOING
        to_customer.html_content = message
        to_customer.reply_to = ContactForm.CONTACT_EMAIL
        to_customer.app = self.__module__
        to_customer.save()


    def send_email_self(self):
        """
        email is send to mentoki
        """
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
            'betreff': "Nachricht an mentoki",
        }
        message = get_template('email/contact/to_mentoki.html').render(Context(context))

        to_mentoki = MailerMessage()
        to_mentoki.subject = "Kontaktanfrage an mentoki"
        to_mentoki.to_address = ContactForm.CONTACT_EMAIL
        to_mentoki.from_address = self.cleaned_data['email']
        to_mentoki.content = ContactForm.INTERNAL
        to_mentoki.html_content = message
        to_mentoki.reply_to = self.cleaned_data['email']
        to_mentoki.app = self.__module__
        to_mentoki.save()











