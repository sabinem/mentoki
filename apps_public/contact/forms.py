# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import floppyforms.__future__ as forms

from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.template import Context


class ContactForm(forms.Form):
    # Kontaktformular

    name = forms.CharField(required=True, max_length=100, label='Name')
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea, label='Ihre Nachricht')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

    def send_email_visitor(self):
        # send email to requesting email
        # this method is called with cleaned from data
        subject = "Deine Nachricht an Mentoki"
        to = [self.cleaned_data['email']]
        from_mail = 'info@mentoki.com'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
            'betreff': "Deine Nachricht",
        }
        message = get_template('email/message_outgoing.html').render(Context(context))
        msg = EmailMessage(subject, message, to=to, from_email=from_mail)
        msg.content_subtype = 'html'
        msg.send()

    def send_email_self(self):
        # send email to self
        subject = "Beantworten: Nachricht an Mentoki"
        to = ['info@mentoki.com']
        from_mail = self.cleaned_data['email']
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
            'betreff': "Nachricht an Mentoki",
        }
        message = get_template('email/message_internal.html').render(Context(context))
        msg = EmailMessage(subject, message, to=to, from_email=from_mail)
        msg.content_subtype = 'html'
        msg.send()











