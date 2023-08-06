from django.db import models
from core.Utils.Mixins.models import CrmMixin, SlugifyMixin, TranslateMixin


class Category(CrmMixin, SlugifyMixin, TranslateMixin):
    TRANSLATED_FIELDS = ['name', 'description']
    SLUGIFY_FIELD = 'name'

    name_data = models.JSONField(default=dict)
    description_data = models.JSONField(default=dict)
    position = models.IntegerField(default=0)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

    @property
    def label(self):
        return str(self)
