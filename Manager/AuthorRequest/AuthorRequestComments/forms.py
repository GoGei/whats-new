import django_filters
from django import forms
from django.utils.translation import ugettext as _
from core.AuthorRequest.models import AuthorRequest, AuthorRequestComment


class AuthorRequestCommentFilterForm(django_filters.FilterSet):
    pass


class AuthorRequestCommentForm(forms.ModelForm):
    class Meta:
        model = AuthorRequestComment
        fields = ('comment',)

    def clean_comment(self):
        data = super().clean()
        comment = data.get('comment')
        comment = comment.strip()
        if not comment:
            self.add_error('comment', _('Comment cannot be empty'))
        return comment


class AuthorRequestCommentFormAdd(AuthorRequestCommentForm):
    def __init__(self, *args, **kwargs):
        self.author_request = kwargs.pop('author_request')
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.author_request = self.author_request
        instance.user = self.user
        if commit:
            instance.save()
        return instance


class AuthorRequestCommentFormEdit(AuthorRequestCommentForm):
    pass
