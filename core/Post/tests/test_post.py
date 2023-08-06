from django.test import TestCase
from ..models import Post
from ..factories import PostFactory


class PostTests(TestCase):
    def test_create(self):
        obj = PostFactory.create()
        qs = Post.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = PostFactory.create()
        obj.delete()

        qs = Post.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = PostFactory.create()
        self.assertTrue(obj.title in str(obj))
        self.assertTrue(obj.title in obj.label)
