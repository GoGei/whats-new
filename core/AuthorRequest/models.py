from html import unescape
from django.db import models
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from core.Utils.Mixins.models import CrmMixin


class AuthorRequest(CrmMixin):
    class WorkingExperienceChoices(models.TextChoices):
        ZERO_TWO = '0_2', _('0-2')
        TWO_FOUR = '2_4', _('2-4')
        FIVE_AND_UP = '5_plus', _('5+')

    class StatusChoices(models.TextChoices):
        NEW = 'new', _('New')
        IN_PROGRESS = 'in_progress', _('In Progress')
        APPROVED = 'approved', _('Approved')
        REJECTED = 'reject', _('Rejected')

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=False, db_index=True)
    phone = models.CharField(max_length=20)
    working_experience = models.CharField(max_length=20, choices=WorkingExperienceChoices.choices)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.NEW, db_index=True)

    class Meta:
        db_table = 'author_request'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def label(self):
        return str(self)

    @property
    def is_allowed_to_interact(self):
        statuses = self.StatusChoices
        return self.status in (statuses.NEW, statuses.IN_PROGRESS)

    def approve(self, modified_by):
        self.status = self.StatusChoices.APPROVED
        self.modify(modified_by)
        return self

    def reject(self, modified_by):
        self.status = self.StatusChoices.REJECTED
        self.archive(modified_by)
        return self


class AuthorRequestComment(CrmMixin):
    COMMENT_STR_LIMIT = 50
    END_COMMENT = '...'

    author_request = models.ForeignKey(AuthorRequest, on_delete=models.PROTECT)
    user = models.ForeignKey('User.User', on_delete=models.PROTECT)
    comment = models.TextField(max_length=2048)

    class Meta:
        db_table = 'author_request_comment'

    def __str__(self):
        comment = self.comment
        lim = self.COMMENT_STR_LIMIT
        end = self.END_COMMENT

        decoded_content = unescape(comment)
        comment = strip_tags(decoded_content)

        comment = comment if len(comment) <= lim else comment[:lim - len(end)] + end
        return comment

    @property
    def label(self):
        return str(self)

    def is_author(self, author) -> bool:
        return author == self.user
