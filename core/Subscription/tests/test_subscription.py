from django.test import TestCase
from django.utils import translation
from core.Category.factories import CategoryFactory
from ..models import Subscription
from ..factories import SubscriptionFactory
from ...Category.models import Category


class SubscriptionTests(TestCase):
    def test_create(self):
        obj = SubscriptionFactory.create()
        qs = Subscription.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = SubscriptionFactory.create()
        obj.delete()

        qs = Subscription.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = SubscriptionFactory.create()
        self.assertTrue(obj.user.email in str(obj))
        self.assertTrue(obj.user.email in obj.label)

        obj.user = None
        obj.save()
        obj.refresh_from_db()
        self.assertTrue(obj.email in str(obj))
        self.assertTrue(obj.email in obj.label)

    def test_categories(self):
        lang = translation.get_language()
        category1 = CategoryFactory.create(name_data={lang: 'category1'})
        category2 = CategoryFactory.create(name_data={lang: 'category2'})
        category3 = CategoryFactory.create(name_data={lang: 'category3'})
        subscription = SubscriptionFactory.create()

        self.assertFalse(subscription.get_categories())
        self.assertFalse(subscription.get_all_categories())

        subscription.add_categories([category1, category3])
        current_categories = subscription.get_categories()
        self.assertTrue(all([category in current_categories for category in [category1, category3]]))
        self.assertEqual(current_categories.count(), 2)

        subscription.add_categories([category3])
        current_categories = subscription.get_categories()
        self.assertTrue(all([category in current_categories for category in [category1, category3]]))
        self.assertEqual(current_categories.count(), 2)

        subscription.remove_categories([category3])
        current_categories = subscription.get_categories()
        self.assertTrue(all([category in current_categories for category in [category1]]))
        self.assertEqual(current_categories.count(), 1)

        subscription.set_categories(Category.objects.filter(id__in=[category2.id, category3.id]))
        current_categories = subscription.get_categories()
        self.assertTrue(all([category in current_categories for category in [category2, category3]]))
        self.assertEqual(current_categories.count(), 2)

        category2.archive()
        category2.refresh_from_db()

        self.assertTrue(all([category in current_categories for category in [category3]]))
        self.assertEqual(subscription.get_categories().count(), 1)
        self.assertEqual(subscription.get_all_categories().count(), 2)

        self.assertRaises(ValueError, subscription.set_categories, categories=[category2, category3])
