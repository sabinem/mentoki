# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import floppyforms.__future__ as forms

from django import forms
from crispy_forms.helper import FormHelper
from apps.forum.models import SubForum



class SubForumCreateForm(forms.ModelForm):

    class Meta:
        model = SubForum
        fields = ('title', 'text', 'parentforum', 'can_have_threads' )

    def __init__(self, *args, **kwargs):
        print "----------- in init"
        forum_id = kwargs.pop('forum_id', None)
        super(SubForumCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_tag = True
        self.helper.form_show_labels = True
        choice_qs = SubForum.objects.filter(forum_id=forum_id)
        self.fields['parentforum'].queryset = choice_qs
        print x

