import django_filters
from django import forms
from ckeditor.widgets import CKEditorWidget
from core.UserFeedback.models import UserFeedback, UserFeedbackReply
from core.Utils.filter_fields import SearchFilterField


class UserFeedbackFilterForm(django_filters.FilterSet):
    search = SearchFilterField()

    class Meta:
        model = UserFeedback
        fields = ('search', 'status')

    def search_qs(self, queryset, name, value):
        return SearchFilterField.search_qs(queryset, name, value,
                                           search_fields=('email', 'first_name', 'last_name'))


class UserFeedbackReplyForm(forms.ModelForm):
    reply = forms.CharField(widget=CKEditorWidget(config_name='user_feedback_reply'), max_length=2048)

    class Meta:
        model = UserFeedbackReply
        fields = ('reply',)

    def __init__(self, *args, **kwargs):
        self.user_feedback = kwargs.pop('user_feedback')
        self.admin = kwargs.pop('admin')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.feedback = self.user_feedback
        instance.admin = self.admin
        if commit:
            instance.save()
        return instance
