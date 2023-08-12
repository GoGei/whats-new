import django_filters
from django import forms
from django.utils.translation import ugettext as _
from core.Colors.models import CategoryColor
from core.Utils.filter_fields import SearchFilterField, IsActiveFilterField


class CategoryColorFilterForm(django_filters.FilterSet):
    search = SearchFilterField()
    is_active = IsActiveFilterField()

    def is_active_filter(self, queryset, name, value):
        return IsActiveFilterField.is_active_filter(queryset, name, value)

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('name', 'value'))


class CategoryColorForm(forms.ModelForm):
    class Meta:
        model = CategoryColor
        fields = ('name', 'value')

    def clean_value(self):
        data = super().clean()
        value = data.get('value')

        try:
            value = CategoryColor.to_hex_color(value)
        except ValueError:
            self.add_error('value', _(f'Passed value is not hex: {value}'))

        if CategoryColor.check_exists(value, instance=self.instance):
            self.add_error('value', _(f'Color with value "{value}" already exists'))

        return value


class CategoryColorFormAdd(CategoryColorForm):
    pass


class CategoryColorFormEdit(CategoryColorForm):
    pass
