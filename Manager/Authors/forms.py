import django_filters
from core.Utils.filter_fields import SearchFilterField


class AuthorFilterForm(django_filters.FilterSet):
    search = SearchFilterField()

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('first_name', 'last_name', 'email'))
