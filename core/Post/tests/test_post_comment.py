from django.test import TestCase
from ..models import PostComment
from ..factories import PostCommentFactory


class PostCommentTests(TestCase):
    def test_create(self):
        obj = PostCommentFactory.create()
        qs = PostComment.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = PostCommentFactory.create()
        obj.delete()

        qs = PostComment.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = PostCommentFactory.create()
        self.assertTrue(obj.content in str(obj))
        self.assertTrue(obj.content in obj.label)

    def test_remove(self):
        obj = PostCommentFactory.create()
        obj.remove()
        self.assertTrue(obj.is_removed)
        self.assertIn('Removed', str(obj))
        obj.undo_remove()
        self.assertFalse(obj.is_removed)
