from unittest.mock import patch, PropertyMock

from django.test import TestCase
from core.Utils.Tests.fuzzy_fields import FuzzyImage
from ..models import Contacts
from ..factories import ContactsFactory


class ContactsTests(TestCase):
    def test_create(self):
        obj = ContactsFactory.create()
        qs = Contacts.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = ContactsFactory.create()
        obj.delete()

        qs = Contacts.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = ContactsFactory.create()
        self.assertTrue(obj.text in str(obj))
        self.assertTrue(obj.text in obj.label)

    def test_validate_file_size(self):
        small_file = FuzzyImage().fuzz()
        large_file = FuzzyImage(size_x=1024, size_y=1024).fuzz()
        with patch.object(Contacts, 'MAX_SIZE', new_callable=PropertyMock(return_value=1024)):
            self.assertTrue(Contacts.validate_file_size(small_file))
            self.assertFalse(Contacts.validate_file_size(large_file))
