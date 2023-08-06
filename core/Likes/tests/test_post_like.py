from django.test import TestCase
from .base_test import BaseLikeTestCase
from ..models import PostLike
from ..factories import PostLikeFactory


class PostLikeTests(BaseLikeTestCase, TestCase):
    MODEL_CLASS = PostLikeFactory

    def test_create(self):
        obj = PostLikeFactory.create()
        qs = PostLike.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = PostLikeFactory.create()
        obj.delete()

        qs = PostLike.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())
