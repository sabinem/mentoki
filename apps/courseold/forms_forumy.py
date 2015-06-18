# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import floppyforms.__future__ as forms

from django import forms
from django.forms import ModelForm
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, HTML, Field, Hidden
from crispy_forms.bootstrap import TabHolder, Tab, InlineField, AppendedText, PrependedText
from apps.forum.models import Post, Thread, SubForum, Forum, calc_subforum_ancestors
from django.forms import ValidationError
from apps.forum.views_forum import ForumMixin
from apps.forum.cachehelpers import calc_real_decendant_ids
from apps.forum.cache import get_forum_structure


class SubForumFormMixin(ForumMixin, forms.ModelForm):

    def clean(self, **kwargs):
        instance = kwargs.get('instance', {})

        cleaned_data = super(SubForumFormMixin, self).clean()
        forumdata = get_forum_structure(forum_id=self.instance.forum_id)
        try:
            parentforum = cleaned_data.get("parentforum").id
            depth_above = forumdata['subforum_dict'][parentforum]['depth_above']
        except:
            depth_above = 0
        try:
             subforum = self.instance.pk
             subforum_depth_below = forumdata['subforum_dict'][subforum]['depth_below']
        except:
             subforum_depth_below = 0
        depth = depth_above + subforum_depth_below + 2
        if depth > 3:
                raise ValidationError(
                   'Die Foren-Tiefe kann im Moment hoechstens 3 betragen.',
                    code='invalid',
                )
        return cleaned_data


class SubForumCompleteUpdateForm(SubForumFormMixin):

    class Meta:
        model = SubForum
        fields = ('title', 'description', 'parentforum', 'can_have_threads' )

    display_number = forms.IntegerField(min_value=1,required=False)
    rearrange_structure = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        forum_id = kwargs.pop('forum_id', None)
        initial = kwargs.get('initial', {})
        instance = kwargs.get('instance', {})
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        real_decendants = calc_real_decendant_ids([instance.id])
        no_choice = real_decendants
        no_choice.append(instance.id)
        choice_qs = SubForum.objects.exclude(id__in=no_choice).filter(forum_id=instance.forum_id)
        super(SubForumCompleteUpdateForm, self).__init__(*args, **kwargs)
        self.fields['parentforum'].queryset = choice_qs


class SubForumReducedUpdateForm(SubForumFormMixin):

    class Meta:
        model = SubForum
        fields = ('title', 'description', 'parentforum' )

    display_number = forms.IntegerField(min_value=1,required=False)
    rearrange_structure = forms.BooleanField(required=False)


    def __init__(self, *args, **kwargs):
        forum_id = kwargs.pop('forum_id', None)
        initial = kwargs.get('initial', {})
        instance = kwargs.get('instance', {})
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        real_decendants = calc_real_decendant_ids([instance.id])
        no_choice = real_decendants
        no_choice.append(instance.id)
        choice_qs = SubForum.objects.exclude(id__in=no_choice).filter(forum_id=instance.forum_id)
        super(SubForumReducedUpdateForm, self).__init__(*args, **kwargs)
        self.fields['parentforum'].queryset = choice_qs



class SubForumCreateForm(forms.ModelForm):

    class Meta:
        model = SubForum
        fields = ('title', 'description', 'parentforum', 'can_have_threads' )

    def __init__(self, *args, **kwargs):
        print "----------- in init"
        forum_id = kwargs.pop('forum_id', None)
        super(SubForumCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_tag = True
        self.helper.form_show_labels = True
        choice_qs = SubForum.objects.filter(forum_id=forum_id)
        self.fields['parentforum'].queryset = choice_qs

