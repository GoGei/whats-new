from factory import fuzzy, DjangoModelFactory, SubFactory
from core.User.factories import UserFactory
from core.Category.factories import CategoryFactory
from core.Utils.Tests.fuzzy_fields import FuzzyLanguage, FuzzyParagraph
from .models import Post, PostComment


class PostFactory(DjangoModelFactory):
    title_data = FuzzyLanguage(FuzzyParagraph, nb_sentences=5, length=128).fuzz()
    description_data = FuzzyLanguage(FuzzyParagraph, nb_sentences=10, length=256).fuzz()
    text_data = FuzzyLanguage(FuzzyParagraph, nb_sentences=5, length=2048).fuzz()
    category = SubFactory(CategoryFactory)
    author = SubFactory(UserFactory)

    class Meta:
        model = Post


class PostCommentFactory(DjangoModelFactory):
    author = SubFactory(UserFactory)
    post = SubFactory(PostFactory)
    parent = None
    content = FuzzyParagraph(length=512)

    class Meta:
        model = PostComment
