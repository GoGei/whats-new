from django.db import models
from core.Utils.Mixins.models import CrmMixin


class Subscription(CrmMixin):
    email = models.EmailField(db_index=True)
    user = models.ForeignKey('User.User', on_delete=models.PROTECT, null=True)
    categories = models.ManyToManyField('Category.Category')

    class Meta:
        db_table = 'subscription'

    def __str__(self):
        return self.user.email if self.user else self.email

    @property
    def label(self):
        return str(self)

    def get_categories(self):
        return self.categories.active().order_by('position')

    def get_all_categories(self):
        return self.categories.all().order_by('position')

    @classmethod
    def check_categories(cls, categories):
        if isinstance(categories, (list, set, tuple)):
            active_categories = list(filter(lambda item: item.is_active() is True, categories))
            is_valid = len(categories) == len(active_categories)
        else:
            is_valid = categories.count() == categories.active().count()

        if not is_valid:
            raise ValueError('It is not allowed to set not active category for subscription')
        return True

    def set_categories(self, categories):
        self.check_categories(categories)
        self.categories.set(categories)
        return self

    def add_categories(self, categories):
        self.check_categories(categories)
        current_categories = self.get_categories()
        for category in categories:
            if category not in current_categories:
                self.categories.add(category)
        return self.get_categories()

    def remove_categories(self, categories):
        self.check_categories(categories)
        current_categories = self.get_categories()
        for category in categories:
            if category in current_categories:
                self.categories.remove(category)
        return self.get_categories()
