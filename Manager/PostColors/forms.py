import json
import django_filters
from django import forms
from django.utils.translation import ugettext as _
from core.Colors.models import PostColor
from core.Utils.filter_fields import SearchFilterField, IsActiveFilterField
from core.Utils.Exporter.importer import CrmMixinJSONLoader


class PostColorFilterForm(django_filters.FilterSet):
    search = SearchFilterField()
    is_active = IsActiveFilterField()

    def is_active_filter(self, queryset, name, value):
        return IsActiveFilterField.is_active_filter(queryset, name, value)

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('name', 'value'))


class PostColorForm(forms.ModelForm):
    class Meta:
        model = PostColor
        fields = ('name', 'value')

    def clean_value(self):
        data = super().clean()
        value = data.get('value')

        try:
            value = PostColor.to_hex_color(value)
        except ValueError:
            self.add_error('value', _(f'Passed value is not hex: {value}'))

        if PostColor.check_exists(value, instance=self.instance):
            self.add_error('value', _(f'Color with value "{value}" already exists'))

        return value


class PostColorFormAdd(PostColorForm):
    pass


class PostColorFormEdit(PostColorForm):
    pass


class PostColorImportForm(forms.Form):
    file = forms.FileField(label=_('File fixture'), required=True,
                           widget=forms.ClearableFileInput(attrs={'accept': '.json',
                                                                  'class': 'form-control file-upload-info'}))

    def clean(self):
        data = self.cleaned_data
        file = data.get('file')

        try:
            content = json.loads(file.read().decode('utf-8'))
            data['content'] = content
        except UnicodeDecodeError:
            self.add_error('file', _('File is not encoded with UTF-8'))
        except (json.JSONDecodeError, ValueError, AttributeError):
            self.add_error('file', _('File is not valid JSON'))

        return data

    def load(self):
        context = self.cleaned_data['content']

        load_fields = ('name', 'value')
        get_by_fields = ('value',)
        items, created_count = CrmMixinJSONLoader(model=PostColor,
                                                  load_fields=load_fields,
                                                  get_by_fields=get_by_fields,
                                                  with_clear=False,
                                                  set_activity=False).load(context)
        return items, created_count
