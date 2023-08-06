from factory import fuzzy, DjangoModelFactory, Faker
from core.Utils.Tests.fuzzy_fields import FuzzyLanguage, FuzzyParagraph
from .models import Category


class CategoryFactory(DjangoModelFactory):
    name_data = FuzzyLanguage(FuzzyParagraph, nb_sentences=5, length=100).fuzz()
    description_data = FuzzyLanguage(FuzzyParagraph, nb_sentences=10, length=1024).fuzz()
    position = fuzzy.FuzzyInteger(low=1, high=99)
    slug = Faker('slug')

    class Meta:
        model = Category
        django_get_or_create = ('slug',)
