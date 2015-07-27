from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db import models
from django.core.validators import RegexValidator

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent


class AccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(username=username, email=self.normalize_email(email),
                          )
        user.is_active = True
        user.set_password(password)
        print "=============="
        print user
        print self._db
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    #obj.course_set.all(): gets all the courses for the account, where he teaches


class Account(AbstractBaseUser, PermissionsMixin):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')

    # redefine fields that would normally be in User
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to="uploads", blank=False, null=False,
                                      default='/static/img/happyface.jpg' )


    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return u'%s' % (self.username)

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
        except:
           return False