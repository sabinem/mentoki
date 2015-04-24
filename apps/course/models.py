# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# import from 3rd party apps
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
# import from other apps
from apps.core.helpers import timesince

def validate_unique(value):
    return None

class CourseBasicModel(TimeStampedModel):
    """
    This is an abstract model for all course parts:
    since courses are the base unit that is very important it is carried in all course parts
    as a foreign key
    """
    text = models.TextField(blank=True, verbose_name='Text')
    STATUS_DRAFT ='0'
    STATUS_READY = '1'
    STATUS = (
        (STATUS_DRAFT, 'Im Aufbau'),
        (STATUS_READY, 'Fertig'),
    )
    status = models.CharField(choices=STATUS, default=STATUS_DRAFT, max_length=2)

    class Meta:
        abstract=True

class Course(CourseBasicModel):
    """
    The course is the key unit for teaching classes. The course contains all the units and materials that
    are being taught for one subject by one teacher. It does not contain a time frame. It is just a pool of
    materials structured into lessons and types of material.
    """
    # each course has a slug
    title = models.CharField(max_length=100, verbose_name='Überschrift')
    slug = models.SlugField(unique=True)
    # these field sum up to the description of the course
    excerpt = models.TextField(blank=True)
    target_group = models.TextField(blank=True)
    prerequisites = models.TextField(blank=True)
    project = models.TextField(blank=True, default="x")
    structure = models.TextField(blank=True)
    # a course has its own email adress, used by the teachers to correspond with its students
    email = models.EmailField(default="info@netteachers.de")
    # a course has a state: is this used at all?

    def __unicode__(self):
        # the course is represented by its title
        return u'%s' % (self.title)

    @property
    def teachers(self):
        # a course may have more then one teacher
        course_owners = CourseOwner.objects.filter(course=self.id)
        teacher_list = []
        for teacher in course_owners:
            teacher_list.append(teacher.user)
        return teacher_list

    @property
    def teachers_display(self):
        # how teachers are displayed
        teachers = self.teachers
        namesstring = ""
        for teacher in teachers:
            if namesstring != "":
                namesstring += " und "
            namesstring += u"%s %s " % (teacher.first_name, teacher.last_name)
        return namesstring


class CoursePartModel(CourseBasicModel):
    """
    This is an abstract model for all course parts:
    since courses are the base unit that is very important it is carried in all course parts
    as a foreign key
    """
    title = models.CharField(max_length=100, verbose_name='Ueberschrift')
    course  = models.ForeignKey(Course, verbose_name='Kurs')
    # will be deleted soon
    display_nr = models.IntegerField(
        verbose_name='interne Nummer, steuert die Anzeigereihenfolge',
    )
    description = models.CharField(max_length=200, blank=True, verbose_name='kurze Beschreibung')

    class Meta:
        abstract=True


class CourseBlock(CoursePartModel):
    """
    There are different blocks of units. A block is units that belong together, such as a version of lessons
    or the organisational units for a courseevent. Blocks will be shown together in the classrooom, but they will
    be released unit by unit if necessary. It is units that belonge together for some reason.
    """
    is_numbered = models.BooleanField(default=True)
    show_full = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s/%s' % (self.course, self.title)


class CourseUnit(CoursePartModel):
    """
    Units are meant to structure courses. There are different kinds of courseunits. Some of them
    are numbered, others are not.
    """
    # will be discontinued
    UNIT_TYPE_LESSON = 'l'
    UNIT_TYPE_ORGANISATION = 'o'
    UNIT_TYPE_BONUS = 'b'
    UNIT_TYPE_CLASSLIST = 'c'
    UNIT_TYPE_COMMUNICATION = 'k'
    UNIT_TYPE_INTERNAL = 'i'
    UNIT_TYPE_SYLLABUS = 's'
    UNIT_TYPE = (
        (UNIT_TYPE_ORGANISATION, 'Organisation'),
        (UNIT_TYPE_LESSON, 'Unterricht'),
        (UNIT_TYPE_BONUS, 'Bonusmaterial'),
        (UNIT_TYPE_CLASSLIST, 'Klassenliste'),
        (UNIT_TYPE_COMMUNICATION, 'Kommunikation'),
        (UNIT_TYPE_INTERNAL, 'Intern'),
        (UNIT_TYPE_SYLLABUS, 'Syllabus'),
    )
    # no longer needed
    unit_type = models.CharField(choices=UNIT_TYPE, default=UNIT_TYPE_LESSON, max_length=2)
    block = models.ForeignKey(CourseBlock, blank=True, null=True, verbose_name='Unterrichtsblock',
                              on_delete=models.SET_NULL)
    # no longer needed
    unit_nr = models.IntegerField(blank=True, null=True, verbose_name='Lektionsnummer')

    def __unicode__(self):

           return u'%s / %s' % (self.block, self.title)


# belongs to course material
def lesson_material_name(instance, filename):
        print instance.course_id
        print instance.course.slug
        path = '/'.join([instance.course.slug, slugify(instance.unit.title), filename])
        print path
        return path


class CourseMaterialUnit(CoursePartModel):
    """
    material like pdf files, etc can only be defined on this sublevel to units.
    """
    unit = models.ForeignKey(CourseUnit, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Lektion")
    # the doc type decides how the document is displayed.
    DOCTYPE_PDFVIEWDOWNLOAD = 'g'
    DOCTYPE_PDFDOWNLOADONLY = '1'
    DOCTYPE_TEXT = 't'
    DOCTYPE = (
        (DOCTYPE_PDFVIEWDOWNLOAD, 'PDF Viewer'),
        (DOCTYPE_PDFDOWNLOADONLY, 'PDF download und Text'),
        (DOCTYPE_TEXT, 'Text'),
    )
    document_type = models.CharField(choices=DOCTYPE,max_length=2, default=DOCTYPE_TEXT, verbose_name="Anzeigemodus")
    # this field can be deleted in the future
    slug = models.SlugField()
    # the file is downloaded at the fileslug
    file = models.FileField(upload_to=lesson_material_name, blank=True, verbose_name="Datei")
    fileslug = AutoSlugField(populate_from='get_file_slug', blank=True)
    sub_unit_nr = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s/%s' % (self.unit, self.title)

    def get_file_slug(instance):
        # the fileslug is determined from the filepath
        pathparts = instance.file.name.split('/')
        fileslug = '-'.join(pathparts)
        return fileslug


# belongs to course material
def course_name(instance, filename):
        print instance.course_id
        print instance.course.slug
        path = '/'.join([instance.course.slug, filename])
        print path
        return path


class CourseOwner(CourseBasicModel):
    """
    The course owners are the teachers teaching the course. This may be moren then one person.
    """
    course = models.ForeignKey(Course)
    user = models.ForeignKey(User)
    foto = models.ImageField(upload_to=course_name, blank=True)
    display = models.BooleanField(default=True)
    display_nr = models.IntegerField(default=1)

    def __unicode__(self):
        # the courseownership is represented by the combination of course and user
        return u'%s %s' % (self.course, self.user)


