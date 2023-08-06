from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.Utils.Mixins.models import CrmMixin


class AuthorRequest(CrmMixin):
    class WorkingExperienceChoices(models.TextChoices):
        ZERO_TWO = '0-2', _('0-2')
        TWO_FOUR = '2-4', _('2-4')
        FIVE_AND_UP = '5+', _('5+')

    class StatusChoices(models.TextChoices):
        NEW = 'new', _('New')
        IN_PROGRESS = 'in_progress', _('In Progress')
        APPROVED = 'approved', _('Approved')
        CANCELED = 'canceled', _('Canceled')

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    phone = models.CharField(max_length=20)
    working_experience = models.CharField(max_length=20, choices=WorkingExperienceChoices.choices)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.NEW)

    class Meta:
        db_table = 'author_request'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def label(self):
        return str(self)


class AuthorRequestComment(CrmMixin):
    COMMENT_STR_LIMIT = 50
    END_COMMENT = '...'

    author_request = models.ForeignKey(AuthorRequest, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    comment = models.TextField(max_length=2048)

    class Meta:
        db_table = 'author_request_comment'

    def __str__(self):
        comment = self.comment
        lim = self.COMMENT_STR_LIMIT
        end = self.END_COMMENT
        comment = comment if len(comment) <= lim else comment[:lim - len(end)] + end
        return comment

    @property
    def label(self):
        return str(self)
