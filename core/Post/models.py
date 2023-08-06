import settings
from django.db import models
from core.Utils.Mixins.models import CrmMixin, SlugifyMixin, TranslateMixin


class Post(CrmMixin, SlugifyMixin, TranslateMixin):
    TRANSLATED_FIELDS = ['title', 'description', 'text']
    SLUGIFY_FIELD = 'title'

    title_data = models.JSONField(default=dict)
    description_data = models.JSONField(default=dict)
    text_data = models.JSONField(default=dict)

    category = models.ForeignKey('Category.Category', on_delete=models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title

    @property
    def label(self):
        return str(self)
