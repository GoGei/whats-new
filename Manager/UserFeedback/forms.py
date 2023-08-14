import django_filters
from core.Utils.filter_fields import SearchFilterField


class UserFeedbackFilterForm(django_filters.FilterSet):
    search = SearchFilterField()

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('email', 'first_name', 'last_name'))
