from django import forms
from django.utils.translation import ugettext as _


class ManagerLoginForm(forms.Form):
    email = forms.EmailField(label=_('Email address'),
                             widget=forms.TextInput({'autofocus': 'autofocus',
                                                     'placeholder': _('Email address')}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput({'placeholder': _('Password')}))
    remember_me = forms.BooleanField(label='Remember me', required=False)

    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email', '')
        return email.lower()
