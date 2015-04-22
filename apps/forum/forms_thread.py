from __future__ import unicode_literals
import floppyforms.__future__ as forms

from django.forms import ModelForm
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab, InlineField, PrependedText
from .models import Thread



class SubforumCompleteLayout(Layout):
   def __init__(self, *args, **kwargs):
        super(SubforumCompleteLayout, self).__init__(
            TabHolder(
                Tab('Beschriftung',
                    PrependedText(
                        'title',
                        'Titel des Unterforums',
                    ),
                    PrependedText(
                        'description',
                        'Beschreibung',
                    ),
                ),
                Tab('Struktur',
                    PrependedText(
                        'parentforum',
                        'Unterforum worunter?',
                    ),
                    PrependedText(
                        'display_number',
                        'an wievielter Stelle?',
                    ),
                    PrependedText(
                        'can_have_threads',
                        'Kann dieses Forum direkt Beitraege haben?',
                    ),
                )
            )

        )



class ThreadUpdateLayout(Layout):

   def __init__(self, *args, **kwargs):
        super(ThreadUpdateLayout, self).__init__(
            TabHolder(
                Tab('Beitrag',
                    InlineField(
                       'title',
                       'text',
                    ),
                ),
                Tab('Struktur',
                    PrependedText(
                        'subforum',
                        'Unterforum',
                    ),
                )
            )

        )


class ThreadCreateLayout(Layout):

   def __init__(self, *args, **kwargs):
        super(ThreadCreateLayout, self).__init__(
                    InlineField(
                        'title',
                        'text',
                    ),
            )


class ThreadCreateForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title', 'text', )

    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_labels = False
    helper.layout = Layout(
        ThreadCreateLayout(),
    )

class ThreadUpdateForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title', 'text', 'subforum' )

    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_labels = False
    helper.layout = Layout(
        ThreadUpdateLayout(),
    )




