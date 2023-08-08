import django_filters
from core.AuthorRequest.models import AuthorRequest
from django.utils.translation import ugettext as _
from core.Utils.filter_fields import SearchFilterField


class AuthorRequestFilterForm(django_filters.FilterSet):
    search = SearchFilterField()
    working_experience = django_filters.ChoiceFilter(label=_('Working experience'), method='working_experience_filter',
                                                     choices=AuthorRequest.WorkingExperienceChoices.choices,
                                                     empty_label=_('Please, select value'))
    status = django_filters.ChoiceFilter(label=_('Status'),
                                         choices=AuthorRequest.StatusChoices.choices,
                                         empty_label=_('Please, select value'))

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('first_name', 'last_name', 'email', 'phone'))

    def working_experience_filter(self, queryset, name, value):
        if value:
            queryset = queryset.filter(working_experience=value)
        return queryset
