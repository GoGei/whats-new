from django.test import TestCase

from ..models import AuthorRequest
from ..factories import AuthorRequestFactory


class AuthorRequestTests(TestCase):
    def test_create(self):
        obj = AuthorRequestFactory.create()
        qs = AuthorRequest.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = AuthorRequestFactory.create()
        obj.delete()

        qs = AuthorRequest.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = AuthorRequestFactory.create()

        self.assertTrue(obj.first_name in str(obj))
        self.assertTrue(obj.last_name in str(obj))

        self.assertTrue(obj.first_name in obj.label)
        self.assertTrue(obj.last_name in obj.label)

    def test_approve(self):
        obj = AuthorRequestFactory.create()
        obj.approve()
        self.assertTrue(obj.status == AuthorRequest.StatusChoices.APPROVED)
        self.assertTrue(obj.is_active)

    def test_cancel(self):
        obj = AuthorRequestFactory.create()
        obj.cancel()
        self.assertTrue(obj.status == AuthorRequest.StatusChoices.CANCELED)
        self.assertFalse(obj.is_active)
