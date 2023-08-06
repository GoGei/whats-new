from django.test import TestCase
from ..models import CategoryColor
from ..factories import CategoryColorFactory


class CategoryColorTestCase(TestCase):
    def test_create(self):
        obj = CategoryColorFactory.create()
        qs = CategoryColor.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = CategoryColorFactory.create()
        obj.delete()

        qs = CategoryColor.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = CategoryColorFactory.create()
        self.assertTrue(obj.value in str(obj))
        self.assertTrue(obj.value in obj.label)
