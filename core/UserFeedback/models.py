from django.db import models
from core.Utils.Mixins.models import CrmMixin


class UserFeedback(CrmMixin):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    feedback = models.TextField(max_length=2048)

    class Meta:
        db_table = 'user_feedback'

    def __str__(self):
        return self.email

    @property
    def label(self):
        return str(self)
