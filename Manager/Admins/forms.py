from typing import Optional

import django_filters
from django import forms
from django.db import models
from django.utils.translation import ugettext as _
from core.User.models import User
from core.Utils.filter_fields import SearchFilterField, IsActiveFilterField, IsFilledFilterForm


class StatusChoices(models.TextChoices):
    STAFF = ('staff', _('Staff'))
    SUPERUSER = ('superuser', _('Superuser'))


class AdminFilterForm(django_filters.FilterSet):
    search = SearchFilterField()
    is_active = IsActiveFilterField()
    is_email_filled = IsFilledFilterForm(label=_('Is email filled'),
                                         method='is_email_filled_filter')
    is_name_filled = IsFilledFilterForm(label=_('Is name filled'),
                                        method='is_name_filled_filter')
    is_phone_filled = IsFilledFilterForm(label=_('Is phone filled'),
                                         method='is_phone_filled_filter')
    admin_status = django_filters.ChoiceFilter(label=_('Admin status'), method='admin_status_filter',
                                               choices=StatusChoices.choices,
                                               empty_label=_('Please, select value')
                                               )

    def is_active_filter(self, queryset, name, value):
        return IsActiveFilterField.is_active_filter(queryset, name, value,
                                                    activity_field='is_active')

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('first_name', 'last_name', 'email', 'phone'))

    def is_email_filled_filter(self, queryset, name, value):
        return IsFilledFilterForm.is_filled_filter(queryset, name, value,
                                                   fields='email')

    def is_name_filled_filter(self, queryset, name, value):
        return IsFilledFilterForm.is_filled_filter(queryset, name, value,
                                                   fields=('first_name', 'last_name'))

    def is_phone_filled_filter(self, queryset, name, value):
        return IsFilledFilterForm.is_filled_filter(queryset, name, value,
                                                   fields='phone')

    def admin_status_filter(self, queryset, name, value):
        if value:
            if value == 'staff':
                queryset = queryset.filter(is_staff=True)
            elif value == 'superuser':
                queryset = queryset.filter(is_superuser=True)
        return queryset


class AdminForm(forms.ModelForm):
    status = forms.ChoiceField(choices=StatusChoices.choices)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone',
                  'is_active', 'status')
        exclude = ('is_staff', 'is_superuser')

    @classmethod
    def to_status(cls, admin) -> Optional[StatusChoices]:
        if admin.is_superuser:
            return StatusChoices.SUPERUSER
        elif admin.is_staff:
            return StatusChoices.STAFF
        else:
            return None

    def clean(self):
        data = super().clean()
        status = data.get('status')
        choices = self.StatusChoices

        if status == choices.STAFF:
            self.instance.is_staff = True
            self.instance.is_superuser = False
        elif status == choices.SUPERUSER:
            self.instance.is_staff = True
            self.instance.is_superuser = True
        else:
            self.add_error('status', _('Invalid status'))
        return data


class AdminFormAdd(AdminForm):
    pass


class AdminFormEdit(AdminForm):
    pass
