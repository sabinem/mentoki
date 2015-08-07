# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.menu import ClassroomMenuItem


class MenuItemForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = ClassroomMenuItem
        fields = ('display_nr', 'display_title', 'item_type',
                  'lesson', 'forum', 'homework',
                  'published', 'is_start_item')
