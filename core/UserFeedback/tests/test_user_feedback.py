from django.test import TestCase
from ..models import UserFeedback
from ..factories import UserFeedbackFactory


class UserFeedbackTests(TestCase):
    def test_create(self):
        obj = UserFeedbackFactory.create()
        qs = UserFeedback.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = UserFeedbackFactory.create()
        obj.delete()

        qs = UserFeedback.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = UserFeedbackFactory.create()
        self.assertTrue(obj.email in str(obj))
        self.assertTrue(obj.email in obj.label)
