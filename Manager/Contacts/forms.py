import django_filters
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, URLValidator
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext as _

from core.Contacts.models import Contacts
from core.Utils.validators import PhoneValidator
from core.Utils.filter_fields import SearchFilterField, IsActiveFilterField


class ContactsFilterForm(django_filters.FilterSet):
    search = SearchFilterField()
    is_active = IsActiveFilterField()

    class Meta:
        model = Contacts
        fields = ('search', 'is_active', 'contact_type')

    def is_active_filter(self, queryset, name, value):
        return IsActiveFilterField.is_active_filter(queryset, name, value)

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('text',))


class ContactsForm(forms.ModelForm):
    icon = forms.ImageField(label=_('Image fixture'), required=False,
                            widget=forms.ClearableFileInput(attrs={'class': 'form-control file-upload-info'}))

    class Meta:
        model = Contacts
        fields = ('text', 'contact_type', 'icon')

    def clean_icon(self):
        data = super().clean()
        icon = data.get('icon')
        if not icon:
            return icon

        if not Contacts.validate_file_size(icon):
            self.add_error('icon', _(f'Icon is too big. Max size is {filesizeformat(Contacts.MAX_SIZE)}'))

        return icon

    def clean(self):
        data = super().clean()

        contact_type = data.get('contact_type')
        choices = Contacts.ContactType
        if contact_type == choices.EMAIL:
            validator = EmailValidator(message=_('Entered incorrect email'))
        elif contact_type == choices.LINK:
            validator = URLValidator(message=_('Entered incorrect URL'))
        elif contact_type == choices.PHONE:
            validator = PhoneValidator(message=_('Entered incorrect phone number'))
        else:
            validator = None
            self.add_error('contact_type', _('Incorrect contact type'))

        if validator:
            text = data.get('text')
            try:
                validator(text)
            except ValidationError:
                self.add_error('text', validator.message)

        return data


class ContactsFormAdd(ContactsForm):
    pass


class ContactsFormEdit(ContactsForm):
    pass
