# coding: utf-8

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
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
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def workers(self, courseevent):
        students = self.courseeventpartcipation_set()
        owners = self.courseowners.all()
        return students

    #obj.course_set.all(): gets all the courses for the account, where he teaches


class User(AbstractBaseUser, PermissionsMixin):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')

    # redefine fields that would normally be in User
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # this field is calculated in the save method, no manual update
    is_teacher = models.BooleanField(default=False, editable=False)

    is_female = models.BooleanField(default=True)

    # this field is calculated in the save method, no manual update
    is_student = models.BooleanField(default=False, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to="uploads", blank=False, null=False,
                                      default='/static/img/happyface.jpg' )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("Benutzer")
        verbose_name_plural = _("Benutzer")

    def __unicode__(self):
        return u'%s' % (self.username)

    def save(self, *args, **kwargs):
    #    if self.teaching():
    #        self.is_teacher = True
    #    if self.studying():
    #        self.is_student = True
    #TODO google considers emails equal even if they have more or less points in them:
    #TODO sabine.m@gmail.com is the same as sabinem@gmail.com
        #self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)


    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def teaching(self):
        return Course.objects.filter(courseowner__user=self)

    def studying(self):
        return CourseEvent.objects.filter(courseeventparticipation__user=self)

    def has_ownership(self, course):
        try:
           Course.objects.get(courseowner__user=self, id=course.id)
           return True
        except Course.DoesNotExist:
           return False
        # Course.object.filter(courseowner__user=self, id=course.id).count() > 0


