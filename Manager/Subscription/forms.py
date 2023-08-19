import django_filters
from django import forms
from django.utils.translation import ugettext_lazy as _
from core.Subscription.models import Subscription
from core.Category.models import Category
from core.Utils.filter_fields import SearchFilterField


class SubscriptionFilterForm(django_filters.FilterSet):
    search = SearchFilterField()
    categories = django_filters.ModelMultipleChoiceFilter(
        label=_('Category'),
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control select2 select2-multiple',
                   'multiple': 'multiple',
                   'placeholder': _('Select categories'),
                   'data-ajax-url': '/api/v1/categories/'}
        )
    )

    class Meta:
        model = Subscription
        fields = ('search', 'categories')

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('email', 'user__email'))
