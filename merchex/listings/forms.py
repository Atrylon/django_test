from unittest.util import _MAX_LENGTH
from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length=1000)
