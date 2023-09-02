from factory import fuzzy, SubFactory, DjangoModelFactory
from core.Utils.Tests.fuzzy_fields import FuzzyEmail, FuzzyParagraph
from core.User.factories import UserFactory
from .models import UserFeedback, UserFeedbackReply


class UserFeedbackFactory(DjangoModelFactory):
    class Meta:
        model = UserFeedback

    email = FuzzyEmail()
    first_name = fuzzy.FuzzyText(length=50)
    last_name = fuzzy.FuzzyText(length=50)
    feedback = FuzzyParagraph(length=2048)


class UserFeedbackReplyFactory(DjangoModelFactory):
    class Meta:
        model = UserFeedbackReply

    admin = SubFactory(UserFactory)
    feedback = SubFactory(UserFeedbackFactory)
    reply = FuzzyParagraph(length=2048)
