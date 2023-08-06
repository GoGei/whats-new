from django.test import TestCase
from ..models import Category
from ..factories import CategoryFactory


class CategoryTests(TestCase):
    def test_create(self):
        obj = CategoryFactory.create()
        qs = Category.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = CategoryFactory.create()
        obj.delete()

        qs = Category.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = CategoryFactory.create()
        self.assertTrue(obj.name in str(obj))
        self.assertTrue(obj.name in obj.label)
