from django.test import TestCase
from ..models import UserFeedback
from ..factories import UserFeedbackFactory
from ...User.factories import UserFactory


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

    def test_can_be_replied(self):
        obj = UserFeedbackFactory.create(status=UserFeedback.Status.NEW)
        self.assertTrue(obj.can_be_replied)

        obj.status = UserFeedback.Status.COMMENTED
        obj.save()
        self.assertFalse(obj.can_be_replied)

    def test_on_view_action(self):
        obj = UserFeedbackFactory.create(status=UserFeedback.Status.NEW)
        user = UserFactory.create()
        obj.on_view_action(user=user)
        self.assertEqual(obj.status, UserFeedback.Status.VIEWED)
        self.assertEqual(obj.admin, user)

    def test_on_reply_action(self):
        obj = UserFeedbackFactory.create(status=UserFeedback.Status.NEW)
        reply = UserFeedbackFactory.create(feedback=obj)
        obj.on_reply_action(reply)
        self.assertEqual(obj.status, UserFeedback.Status.COMMENTED)
        self.assertEqual(obj.admin, reply.admin)
