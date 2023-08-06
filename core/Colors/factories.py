from factory import fuzzy, DjangoModelFactory
from .models import CategoryColor, PostColor
from core.Utils.Tests.fuzzy_fields import FuzzyColor


class BaseColorFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=50)
    value = FuzzyColor()


class CategoryColorFactory(BaseColorFactory):
    class Meta:
        model = CategoryColor


class PostColorFactory(BaseColorFactory):
    class Meta:
        model = PostColor
