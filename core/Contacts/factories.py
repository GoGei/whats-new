from factory import fuzzy, django, DjangoModelFactory
from .models import Contacts


class ContactsFactory(DjangoModelFactory):
    text = fuzzy.FuzzyText(length=255)
    contact_type = fuzzy.FuzzyChoice(dict(Contacts.ContactType.choices).keys())
    icon = django.ImageField()

    class Meta:
        model = Contacts
