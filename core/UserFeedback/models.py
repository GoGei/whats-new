from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.Utils.Mixins.models import CrmMixin


class UserFeedback(CrmMixin):
    class Status(models.TextChoices):
        NEW = 'new', _('New')
        VIEWED = 'viewed', _('Viewed')
        COMMENTED = 'commented', _('Commented')

    email = models.EmailField(db_index=True)
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    feedback = models.TextField(max_length=2048)

    status = models.CharField(max_length=16, choices=Status.choices, default=Status.NEW)
    admin = models.ForeignKey('User.User', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'user_feedback'

    def __str__(self):
        return self.email

    @property
    def label(self):
        return str(self)

    @property
    def can_be_replied(self):
        return self.status != self.Status.COMMENTED

    def on_view_action(self, user):
        if self.status == self.Status.NEW:
            self.status = self.Status.VIEWED
            self.admin = user
            self.save()
        return self

    def on_reply_action(self, reply):
        self.status = self.Status.COMMENTED
        self.admin = reply.admin
        self.save()
        return self


class UserFeedbackReply(CrmMixin):
    admin = models.ForeignKey('User.User', on_delete=models.PROTECT)
    feedback = models.ForeignKey(UserFeedback, on_delete=models.PROTECT)
    reply = models.TextField(max_length=2048)

    class Meta:
        db_table = 'user_feedback_reply'

    def __str__(self):
        return f'Reply to {self.feedback}'

    @property
    def label(self):
        return str(self)
