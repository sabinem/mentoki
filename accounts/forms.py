# coding: utf-8

"""
Forms for Custom User Model
"""
from __future__ import unicode_literals, absolute_import

import floppyforms.__future__ as forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from .models import User as MentokiUser

import logging
logger = logging.getLogger('activity.usersignup')


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = MentokiUser
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            MentokiUser._default_manager.get(username=username)
        except MentokiUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages('Duplicate username'))

    def clean_password2(self):
        #check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match')

    def save(self,commit=True):
        # save the provided password in hashed format
        user = super(CustomUserCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        logging.info('Benutzer [%s]: neues Passwort' % self)
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    """
    Change Form for Custom User Model
    """
    password = ReadOnlyPasswordHashField(label="password",
                                         help_text="""Raw passwords are not stored, so there is no way to see this
                                         user's password, but you can change the password using <a href=\"password/\">
                                         this form</a>.""")

    class Meta(UserChangeForm.Meta):
        model = MentokiUser
        fields = ('username', 'email', 'password', 'is_teacher',
                  'is_active', 'is_staff', 'is_superuser', 'user_permissions')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class SignupForm(forms.Form):
    """
    User Signup Form
    """
    first_name = forms.CharField(
        label='Vorname',
        max_length=30,
        widget=forms.TextInput(
           attrs={'placeholder':
                  'Vorname',
                  'autofocus': 'autofocus'}))
    last_name = forms.CharField(
        label='Nachname',
        max_length=30,
        widget=forms.TextInput(
           attrs={'placeholder':
                  'Nachname'}))

    def signup(self, request, user):
        """
        signup of users
        if an anonymous user was redirected to the signup form, it is
        memorized, what he wanted to buy in the "unfinshed_product_pk".
        :param request:
        :param user:
        :return: None
        """
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if request.session.has_key('unfinished_checkout'):

            user.checkout_product_pk=\
                request.session['unfinished_product_pk']
            logger.info('Benutzer [%s] wird gespeichert mit Wunsch: [%s]'
                                % (user, user.checkout_product_pk))
        user.save()