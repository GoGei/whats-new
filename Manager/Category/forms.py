import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from core.Category.models import Category
from core.Colors.models import CategoryColor
from core.Utils.filter_fields import SearchFilterField, IsActiveFilterField


class CategoryFilterForm(django_filters.FilterSet):
    search = SearchFilterField()
    is_active = IsActiveFilterField()
    color = django_filters.ModelChoiceFilter(
        label=_('Color'),
        queryset=CategoryColor.objects.active(),
        empty_label=_('Select a color'),
        widget=forms.Select(
            attrs={'class': 'form-control select2',
                   'placeholder': _('Select a color'),
                   'data-ajax-url': '/api/v1/category-colors/'}
        )
    )

    class Meta:
        model = Category
        fields = ('search', 'is_active', 'color')

    def is_active_filter(self, queryset, name, value):
        return IsActiveFilterField.is_active_filter(queryset, name, value)

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('name_data',))


class CategoryForm(forms.ModelForm):
    color = forms.ModelChoiceField(
        label=_('Color'),
        queryset=CategoryColor.objects.active(),
        empty_label=_('Select a color'),
        widget=forms.Select(
            attrs={'class': 'form-control select2',
                   'placeholder': _('Select a color'),
                   'data-ajax-url': '/api/v1/category-colors/'}
        )
    )

    class Meta:
        model = Category
        fields = ('name_data', 'description_data', 'position', 'color', 'slug')

    def clean_slug(self):
        slug = Category.value_to_slug(self.cleaned_data.get('slug'))
        if not Category.is_allowed_to_assign_slug(slug, self.instance):
            self.add_error('slug', _('It is not allowed to assign slug'))
        return slug


class CategoryFormAdd(CategoryForm):
    pass


class CategoryFormEdit(CategoryForm):
    pass
