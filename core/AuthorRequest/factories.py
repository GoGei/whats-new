from factory import fuzzy, SubFactory, DjangoModelFactory
from core.User.factories import UserFactory
from core.Utils.Tests.fuzzy_fields import FuzzyEmail, FuzzyPhone, FuzzyParagraph
from .models import AuthorRequest, AuthorRequestComment


class AuthorRequestFactory(DjangoModelFactory):
    class Meta:
        model = AuthorRequest

    first_name = fuzzy.FuzzyText(length=50)
    last_name = fuzzy.FuzzyText(length=50)
    email = FuzzyEmail()
    phone = FuzzyPhone(length=12)
    working_experience = fuzzy.FuzzyChoice(dict(AuthorRequest.WorkingExperienceChoices.choices).keys())
    status = fuzzy.FuzzyChoice(dict(AuthorRequest.StatusChoices.choices).keys())


class AuthorRequestCommentFactory(DjangoModelFactory):
    class Meta:
        model = AuthorRequestComment

    author_request = SubFactory(AuthorRequestFactory)
    user = SubFactory(UserFactory)
    comment = FuzzyParagraph(length=1024)
