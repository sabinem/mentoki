# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import floppyforms.__future__ as forms
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, HTML
from crispy_forms.bootstrap import TabHolder, Tab
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.template import Context
import floppyforms.__future__ as forms
# import from django
from django.forms import ModelForm
from django import forms
# from 3rd party apps
from crispy_forms.helper import FormHelper
# import from this app
from .models import Contact
from apps.courseevent.models import CourseEvent


class ApplicationForm(forms.ModelForm):

    class Meta:
        fields = ('name', 'email', 'projecttype',
                  'projectdescription', 'qualification', 'motivation',
                  'priorexperience', 'contactinfo', )
        model = Contact

    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_labels = False

    def send_email_visitor(self):
        # send email to requesting email
        # this method is called with cleaned from data
        subject = "Ihre Nachricht an Mentoki"
        to = [self.cleaned_data['email']]
        from_mail = 'info@mentoki.com'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'contactinfo': self.cleaned_data['contactinfo'],
            'betreff': "Ihre Nachricht",
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
            'contactinfo': self.cleaned_data['contactinfo'],
            'betreff': "Nachricht an Mentoki",
        }
        message = get_template('email/message_internal.html').render(Context(context))
        msg = EmailMessage(subject, message, to=to, from_email=from_mail)
        msg.content_subtype = 'html'
        msg.send()


class ContactForm(forms.ModelForm):

    class Meta:
        fields = ('name', 'email', 'message')
        model = Contact

    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True

    def send_email_visitor(self):
        # send email to requesting email
        # this method is called with cleaned from data
        subject = "Ihre Nachricht an Mentoki"
        to = [self.cleaned_data['email']]
        from_mail = 'info@mentoki.com'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
            'betreff': "Ihre Nachricht",
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


class PrebookForm(forms.ModelForm):

    class Meta:
        fields = ('name', 'email', 'message', 'courseevent')
        model = Contact

    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True

    def __init__(self, *args, **kwargs):
        super(PrebookForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial', {})
        self.helper = FormHelper(form=self)
        self.helper.form_tag = False
        self.helper.form_show_labels = True
        # only blocks from the same course can be associated
        self.fields['courseevent'].queryset = \
            CourseEvent.objects.filter(status_external=CourseEvent.EXTEVENT_PREVIEW)

    def send_email_visitor(self):
        # send email to requesting email
        # this method is called with cleaned from data
        subject = "Ihre Nachricht an Mentoki"
        to = [self.cleaned_data['email']]
        from_mail = 'info@mentoki.com'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
            'betreff': "Ihre Nachricht",
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
