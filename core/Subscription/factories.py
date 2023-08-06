from factory import DjangoModelFactory, SubFactory
from core.Utils.Tests.fuzzy_fields import FuzzyEmail
from core.User.factories import UserFactory
from .models import Subscription


class SubscriptionFactory(DjangoModelFactory):
    email = FuzzyEmail()
    user = SubFactory(UserFactory)

    class Meta:
        model = Subscription
