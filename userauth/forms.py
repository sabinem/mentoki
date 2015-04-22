from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput,
        required=False,
        label="",
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.TextInput,
        required=False,
        label="",
    )
