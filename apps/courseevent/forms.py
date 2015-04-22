import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core.urlresolvers import reverse


"""
There is a simple search form on the home page.
"""
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class SearchForm(forms.Form):
    """
    Simple searchform for the homepage with just one searchfield.
    The action is a redirect to the searchpage.
    """
    searchterm = forms.CharField(
        max_length=100,
        widget=forms.TextInput,
        required=False,
        label="",
    )
    helper = FormHelper()

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        # redirect to the searchpage
        self.helper.form_action =  reverse('courseevent:list')
        self.helper.form_method = "get"
        self.helper.form_id = "searchform"
        self.helper.layout = Layout(
            'searchterm',
            Submit('suchen', 'Suchen Sie in unseren Kursen!', css_class='btn-success'),
        )