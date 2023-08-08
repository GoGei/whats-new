# from django import forms
# from django.forms import formset_factory
# from django.forms.formsets import BaseFormSet
# from django.shortcuts import render
#
# from core.Category.models import Category
# from django.conf import settings
# from django.utils.translation import ugettext as _
#
#
# class BaseLangForm(forms.Form):
#     language_code = forms.CharField(widget=forms.HiddenInput)
#
#     def __init__(self, *args, **kwargs):
#         super(BaseLangForm, self).__init__(*args, **kwargs)
#         if self.initial.get('language_code') != settings.DEFAULT_LANGUAGE:
#             for key, field in self.fields.items():
#                 if key != 'language_code':
#                     field.required = False
#
#     def save(self, obj):
#         data = self.cleaned_data
#         language_code = data['language_code']
#         for field in obj.TRANSLATED_FIELDS:
#             if field in self.fields:
#                 getattr(obj, '%s_data' % field)[language_code] = data[field]
#         obj.save()
#
#
# class BaseLangFormSet(BaseFormSet):
#
#     def __init__(self, *args, **kwargs):
#         initial = kwargs.pop('initial', None)
#         instance = kwargs.pop('instance', None)
#         self.can_delete = True
#         if 'can_delete' in kwargs:
#             self.can_delete = kwargs.pop('can_delete')
#
#         if not initial:
#             allowed_languages = list(zip(*settings.LANGUAGES))[0]
#             initial = [{'language_code': language} for language in allowed_languages]
#
#         if instance:
#             initial = instance.get_form_initial()
#
#         super(BaseLangFormSet, self).__init__(*args, initial=initial, **kwargs)
#
#     def clean(self):
#         fields = Category.TRANSLATED_FIELDS
#         for field in fields:
#             if not any([bool(form.cleaned_data.get(field, None)) for form in self.forms]):
#                 for form in self.forms:
#                     form.add_error(field, _("Add at least one translation"))
#
#         if any(self.errors):
#             return
#         if not any([not form.cleaned_data.get('delete') for form in self.forms]):
#             raise forms.ValidationError(_("Set any value."))
#
#     def get_forms(self):
#         return [_form for _form in self.forms if _form.cleaned_data]
#
#     def save(self, obj):
#         for form in self.get_forms():
#             data = form.cleaned_data
#             if data['language_code']:
#                 form.save(obj)
#
#
# class CategoryLangForm(BaseLangForm):
#     name = forms.CharField(label=_('Name'), max_length=200, required=False)
#     description = forms.CharField(label=_('description'), max_length=200, required=False)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.model = Category
#
#     def clean(self):
#         data = super().clean()
#         self.add_error('data', data)
#         return data
#
#
# class CategoryLangFormSet(BaseLangFormSet):
#     pass
#
#
# CategoryLangFormSetFactory = formset_factory(CategoryLangForm, formset=CategoryLangFormSet, extra=0)
#
#
# def manager_test(request):
#     lang_form_set = CategoryLangFormSetFactory(request.POST or None,
#                                                request.FILES or None,
#                                                prefix='category',
#                                                can_delete=False)
#     print('there')
#     if lang_form_set.is_valid():
#         print('valid')
#         print(lang_form_set.cleaned_data)
#         print(lang_form_set.is_valid())
#     else:
#         print('errors')
#         print(lang_form_set.errors)
#
#     return render(request, 'Manager/manager_test.html', {'formset': lang_form_set})


# from core.Category.models import Category
# from django import forms
# from django.conf import settings
# from django.forms.formsets import BaseFormSet
# from django.utils.translation import ugettext_lazy as _
# from django.forms.formsets import formset_factory
# from django.contrib import messages
# from django.shortcuts import render
#
#
# class BaseLangForm(forms.Form):
#     language_code = forms.CharField(widget=forms.HiddenInput)
#
#     def __init__(self, *args, **kwargs):
#         super(BaseLangForm, self).__init__(*args, **kwargs)
#         if self.initial.get('language_code') != settings.DEFAULT_LANGUAGE:
#             for key, field in self.fields.items():
#                 if key != 'language_code':
#                     field.required = False
#
#     def save(self, obj):
#         data = self.cleaned_data
#         language_code = data['language_code']
#         for field in obj.TRANSLATED_FIELDS:
#             if field in self.fields:
#                 getattr(obj, '%s_data' % field)[language_code] = data[field]
#         obj.save()
#
#
# class BaseLangFormSet(BaseFormSet):
#
#     def __init__(self, *args, **kwargs):
#         initial = kwargs.pop('initial', None)
#         instance = kwargs.pop('instance', None)
#         self.can_delete = True
#         if 'can_delete' in kwargs:
#             self.can_delete = kwargs.pop('can_delete')
#
#         if not initial:
#             allowed_languages = list(zip(*settings.LANGUAGES))[0]
#             initial = [{'language_code': language} for language in allowed_languages]
#             print('initial', initial)
#
#         if instance:
#             initial = instance.get_form_initial()
#
#         super(BaseLangFormSet, self).__init__(*args, initial=initial, **kwargs)
#
#     def clean(self):
#         if any(self.errors):
#             print('BaseLangFormSet clean')
#             return self.cleaned_data
#         if not any([not form.cleaned_data.get('delete') for form in self.forms]):
#             raise forms.ValidationError(_("Set any value."))
#
#     def get_forms(self):
#         return [_form for _form in self.forms if _form.cleaned_data]
#
#     def save(self, obj):
#         for form in self.get_forms():
#             data = form.cleaned_data
#             if data['language_code']:
#                 form.save(obj)
#
#
# class CategoryLangForm(forms.Form):
#     language_code = forms.CharField(label=_('Language'), widget=forms.HiddenInput)
#     name = forms.CharField(label=_('Name'), max_length=30)
#
#     def __init__(self, *args, **kwargs):
#         super(self.__class__, self).__init__(*args, **kwargs)
#         self.model = Category
#
#     def clean(self):
#         if any(self.errors):
#             return
#         data = self.cleaned_data
#         return data
#
#     def save(self, obj):
#         data = self.cleaned_data
#         language_code = data['language_code']
#         obj.name_data[language_code] = data['name']
#         obj.save()
#         return None
#
#
# class CategoryFormSet(BaseLangFormSet):
#     def save(self, obj):
#         for form in self.get_forms():
#             data = form.cleaned_data
#             if data['language_code'] and data['name']:
#                 form.save(obj)
#
#     def clean(self):
#         print('data', self.data)
#         return super().clean()
#
#
# CategoryLangFormSet = formset_factory(CategoryLangForm, formset=CategoryFormSet, extra=0)
#
#
# def manager_test(request):
#     formset = CategoryLangFormSet(request.POST or None,
#                                   request.FILES or None,
#                                   prefix='category',
#                                   can_delete=False)
#
#     print(request.POST)
#
#     if formset.is_valid():
#         print('cleaned_data', formset.cleaned_data)
#         messages.success(request, formset.cleaned_data)
#     else:
#         print('errors', formset.errors)
#         messages.error(request, formset.errors)
#         print('formset', formset)
#
#     return render(request,
#                   'Manager/manager_test.html',
#                   {'formset': formset})

from django import forms


class MyForm(forms.Form):
    field1 = forms.CharField()
    # Add more fields as needed


from django.forms.formsets import BaseFormSet


class MyFormSet(BaseFormSet):

    def __init__(self, *args, **kwargs):
        super(MyFormSet, self).__init__(*args, **kwargs)

        # Customize labels for the language
        for form in self.forms:
            language_code = form.cleaned_data['language_code']
            form.fields['field1'].label = 'Field 1 ({})'.format(language_code.upper())


from django.utils.translation import ugettext_lazy as _


class LanguageForm(forms.Form):
    language_code = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)
        self.fields['language_code'].initial = kwargs.get('prefix', '')

    def get_form(self, language_code):
        return MyForm(prefix=language_code)


from django.forms import formset_factory
from django.conf import settings

# Create a common "language" form instance
language_form = LanguageForm()

# Create the formset using formset_factory and the custom MyFormSet
MyLangFormSet = formset_factory(language_form.get_form, formset=MyFormSet, extra=0, can_delete=False)

from django.shortcuts import render
from django.contrib import messages


def manager_test(request):
    formset = MyLangFormSet(request.POST, prefix='language')
    if formset.is_valid():
        print('cleaned_data', formset.cleaned_data)
        messages.success(request, formset.cleaned_data)
    else:
        print('errors', formset.errors)
        messages.error(request, formset.errors)

    return render(request,
                  'Manager/manager_test.html',
                  {'formset': formset})
