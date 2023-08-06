from factory import fuzzy, DjangoModelFactory
from core.Utils.Tests.fuzzy_fields import FuzzyEmail, FuzzyParagraph
from .models import UserFeedback


class UserFeedbackFactory(DjangoModelFactory):
    class Meta:
        model = UserFeedback

    email = FuzzyEmail()
    first_name = fuzzy.FuzzyText(length=50)
    last_name = fuzzy.FuzzyText(length=50)
    feedback = FuzzyParagraph(length=2048)
