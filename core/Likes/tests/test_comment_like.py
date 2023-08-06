from django.test import TestCase
from .base_test import BaseLikeTestCase
from ..models import CommentLike
from ..factories import CommentLikeFactory


class CommentLikeTests(BaseLikeTestCase, TestCase):
    MODEL_CLASS = CommentLikeFactory

    def test_create(self):
        obj = CommentLikeFactory.create()
        qs = CommentLike.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = CommentLikeFactory.create()
        obj.delete()

        qs = CommentLike.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())
