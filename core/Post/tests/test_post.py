from django.test import TestCase
from ..models import Post
from ..factories import PostFactory, PostCommentFactory


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

    def test_by_creator(self):
        obj = PostFactory.create()
        self.assertIs(obj.by_the_creator, False)

        obj.set_by_creator()
        self.assertIs(obj.by_the_creator, True)

        obj.unset_by_creator()
        self.assertIs(obj.by_the_creator, False)

    def test_get_comments(self):
        obj = PostFactory.create()
        comment1 = PostCommentFactory.create(post=obj)
        comment2 = PostCommentFactory.create(post=obj)
        comment2.archive()
        comment3 = PostCommentFactory.create()
        qs = obj.get_comments()
        self.assertTrue(comment1 in qs)
        self.assertTrue(comment2 in qs)
        self.assertFalse(comment3 in qs)
