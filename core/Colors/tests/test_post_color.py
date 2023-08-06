from django.test import TestCase
from ..models import PostColor
from ..factories import PostColorFactory


class PostColorTestCase(TestCase):
    def test_create(self):
        obj = PostColorFactory.create()
        qs = PostColor.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = PostColorFactory.create()
        obj.delete()

        qs = PostColor.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = PostColorFactory.create()
        self.assertTrue(obj.value in str(obj))
        self.assertTrue(obj.value in obj.label)
