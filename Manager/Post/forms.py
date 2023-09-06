import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from core.Category.models import Category
from core.Colors.models import PostColor
from core.User.models import User
from core.Post.models import Post
from core.Utils.filter_fields import SearchFilterField, IsActiveFilterField


class PostFilterForm(django_filters.FilterSet):
    search = SearchFilterField()
    is_active = IsActiveFilterField()
    category = django_filters.ModelChoiceFilter(
        label=_('Category'),
        queryset=Category.objects.active(),
        empty_label=_('Select a category'),
        widget=forms.Select(
            attrs={'class': 'form-control select2',
                   'placeholder': _('Select a category'),
                   'data-ajax-url': '/api/v1/categories/'}
        )
    )
    color = django_filters.ModelChoiceFilter(
        label=_('Color'),
        queryset=Category.objects.active(),
        empty_label=_('Select a color'),
        widget=forms.Select(
            attrs={'class': 'form-control select2',
                   'placeholder': _('Select a color'),
                   'data-ajax-url': '/api/v1/post-colors/'}
        )
    )

    class Meta:
        model = Post
        fields = ('search', 'is_active', 'category')

    def is_active_filter(self, queryset, name, value):
        return IsActiveFilterField.is_active_filter(queryset, name, value)

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('title_data', 'slug'))


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label=_('Category'),
        queryset=Category.objects.active(),
        empty_label=_('Select a category'),
        widget=forms.Select(
            attrs={'class': 'form-control select2',
                   'placeholder': _('Select a category'),
                   'data-ajax-url': '/api/v1/categories/'}
        )
    )
    author = forms.ModelChoiceField(
        label=_('Author'),
        queryset=User.objects.authors_or_admins().filter(is_active=True),
        empty_label=_('Select an author'),
        widget=forms.Select(
            attrs={'class': 'form-control select2',
                   'placeholder': _('Select an author'),
                   'data-ajax-url': '/api/v1/users/'}
        )
    )
    color = forms.ModelChoiceField(
        label=_('Color'),
        queryset=PostColor.objects.active(),
        empty_label=_('Select a color'),
        widget=forms.Select(
            attrs={'class': 'form-control select2',
                   'placeholder': _('Select a color'),
                   'data-ajax-url': '/api/v1/post-colors/'}
        )
    )

    class Meta:
        model = Post
        fields = ('title_data', 'description_data', 'text_data',
                  'category', 'author', 'color', 'slug')

    def clean_slug(self):
        slug = Post.value_to_slug(self.cleaned_data.get('slug'))
        if not Post.is_allowed_to_assign_slug(slug, self.instance):
            self.add_error('slug', _('It is not allowed to assign slug'))
        return slug


class PostFormAdd(PostForm):
    pass


class PostFormEdit(PostForm):
    pass
