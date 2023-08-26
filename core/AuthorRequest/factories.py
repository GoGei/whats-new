from factory import fuzzy, SubFactory, DjangoModelFactory, LazyAttribute
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
    user = LazyAttribute(
        lambda o: UserFactory.create(
            first_name=o.first_name,
            last_name=o.last_name,
            email=o.email,
            phone=o.phone,
        ) if o.status == AuthorRequest.StatusChoices.APPROVED else None)


class AuthorRequestCommentFactory(DjangoModelFactory):
    class Meta:
        model = AuthorRequestComment

    author_request = SubFactory(AuthorRequestFactory)
    user = SubFactory(UserFactory)
    comment = FuzzyParagraph(length=1024)
