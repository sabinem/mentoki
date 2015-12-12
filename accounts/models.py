# coding: utf-8

"""
Custom user model. Login with email. Also a profile picture and fields for
roles at the platform are added.
"""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent

from .constants import StartDesk
from django_enumfield import enum

import logging
logger = logging.getLogger('activity.usersignup')


class UserManager(BaseUserManager):
    """
    Manager for Custom User Model
    """
    def create_user(self, username, email, first_name, last_name, password=None):
        """
        Create user
        :param username:
        :param email:
        :param first_name:
        :param last_name:
        :param password, optional
        :return: user
        """
        #TODO Do I need that?
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(username=username,
                          email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name
                          )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        logging.info('Benutzer wurde angelegt [%s]' % user)
        return user

    def create_superuser(self, username, email, password):
        """
        Create superuser
        :param username:
        :param email:
        :param password, optional:
        :return: user
        """
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        logging.info('Superuser wurde angelegt [%s]' % user)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    """
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')

    # redefine fields that would
    # normally be in User
    email = models.EmailField(
        unique=True
    )
    username = models.CharField(
        verbose_name='Benutzername',
        max_length=40,
        unique=True
    )
    first_name = models.CharField(
        max_length=40,
        blank=True
    )
    last_name = models.CharField(
        max_length=40,
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    # fields that are so far entered manually
    is_teacher = models.BooleanField(
        default=False
    )
    is_female = models.BooleanField(
        default=True
    )
    is_student = models.BooleanField(
        default=False
    )
    # timestamp fields
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    # profile picture used in ths forum and the like
    profile_image = models.ImageField(
        verbose_name='Profilbild',
        upload_to="uploads",
        blank=True,
        null=True,
        )
    # a product that an anonymous user wanted to buy is
    # memorized until he is registered
    checkout_product_pk = models.IntegerField(
        blank=True, null=True
    )
    #TODO: remove this field?
    # this field is not use so far, it is meant to determine a users
    # preference about what is on his desk when he logs in
    start_desk = enum.EnumField(
        StartDesk,
        default=StartDesk.INITIAL
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("Benutzer")
        verbose_name_plural = _("Benutzer")

    def __unicode__(self):
        return u'%s' % (self.username)

    def save(self, *args, **kwargs):
        """
        save method for users, so far just super is called
        """
        #TODO which emails should be considered as equal?
        #self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    def get_full_name(self):
            return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        """
        gets the first name of a user
        :return: first name
        """
        return self.first_name

    def teaching(self):
        """
        Courses that user is teaching
        :return: queryset for Course
        """
        return Course.objects.filter(courseowner__user=self)

    def studying(self):
        """
        CourseEvents that user is participating in
        :return: queryset for CourseEvent
        """
        return CourseEvent.objects.filter(courseeventparticipation__user=self)



