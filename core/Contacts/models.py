from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.Utils.Mixins.models import CrmMixin


class Contacts(CrmMixin):
    MAX_SIZE = 1024 * 1024 * 5  # 5mb

    class ContactType(models.TextChoices):
        email = 'email', _('Email')
        phone = 'phone', _('Phone')
        link = 'link', _('Link')

    text = models.CharField(max_length=255, db_index=True)
    contact_type = models.CharField(choices=ContactType.choices, max_length=10, db_index=True)
    icon = models.ImageField(upload_to=settings.CONTACT_ICONS_FOLDER, null=True)

    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return f'{self.text} ({self.get_contact_type_display()})'

    @property
    def label(self):
        return str(self)

    @classmethod
    def validate_file_size(cls, file) -> bool:
        if file.size > cls.MAX_SIZE:
            return False
        return True
