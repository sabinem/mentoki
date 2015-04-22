# In some models.py...
import datetime
from django.db import models

class Document(models.Model):
    """A sample model with a FileField."""
    slug = models.SlugField(verbose_name='slug')
    file = models.FileField(verbose_name='file', upload_to='document')

    def __unicode__(self):
        return '%s' % (self.slug)


class Image(models.Model):
    image = models.FileField(upload_to='image')





class File(models.Model):

    upload = models.FileField(upload_to="uploads/%Y/%m/%d/")
    date_created = models.DateTimeField(default=datetime.datetime.now)
    is_image = models.BooleanField(default=True)