import re
from django.db import models
from core.Utils.Mixins.models import CrmMixin


class ColorAbstract(CrmMixin):
    name = models.CharField(max_length=50, db_index=True)
    value = models.CharField(max_length=7, db_index=True)

    class Meta:
        abstract = True

    @classmethod
    def to_hex_color(cls, value):
        _value = value.strip().upper()
        if '#' not in _value:
            _value = '#' + _value

        pattern = re.compile(r'^#([A-F0-9]{6})$')
        result = pattern.match(_value)

        if not result:
            raise ValueError(f'Passed value is not hex: {value}')

        return _value

    @classmethod
    def check_exists(cls, value, instance=None) -> bool:
        qs = cls.objects.filter(value=value)
        if instance:
            qs = qs.exclude(id=instance.id)
        return qs.exists()

    def __str__(self):
        return self.value

    @property
    def label(self):
        return str(self)


class CategoryColor(ColorAbstract):
    class Meta:
        db_table = 'category_color'


class PostColor(ColorAbstract):
    class Meta:
        db_table = 'post_color'
