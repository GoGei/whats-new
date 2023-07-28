import django_filters
from django import forms
from django.db.models import Q
from django.utils.translation import ugettext as _


class UserFilterForm(django_filters.FilterSet):
    search = django_filters.CharFilter(label=_('Search'), method='search_qs',
                                       widget=forms.TextInput(attrs={
                                           'type': 'search', 'class': 'form-control', 'placeholder': _('Search')
                                       }))
    is_active = django_filters.BooleanFilter(label=_('Is active'), method='is_active_filter',
                                             widget=forms.Select(attrs={
                                                 'class': 'form-control'},
                                                 choices=[(None, _('Select')), (True, _('Active')),
                                                          (False, _('Not active'))])
                                             )

    def __init__(self, *args, **kwargs):
        self.search_fields = kwargs.pop('search_fields')
        super().__init__(*args, **kwargs)

    def is_active_filter(self, queryset, name, value):
        if isinstance(value, bool):
            queryset = queryset.filter(is_active=value)
        return queryset

    def search_qs(self, queryset, name, value):
        fields = self.search_fields
        _filter = Q()
        for field in fields:
            _filter |= Q(**{f'{field}__icontains': value})
        queryset = queryset.filter(_filter)
        return queryset
