from django.test import TestCase
from ..models import UserFeedbackReply
from ..factories import UserFeedbackReplyFactory


class UserFeedbackReplyTests(TestCase):
    def test_create(self):
        obj = UserFeedbackReplyFactory.create()
        qs = UserFeedbackReply.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = UserFeedbackReplyFactory.create()
        obj.delete()

        qs = UserFeedbackReply.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = UserFeedbackReplyFactory.create()
        self.assertTrue(obj.feedback.label in str(obj))
        self.assertTrue(obj.feedback.label in obj.label)
