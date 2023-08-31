from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel
from core.Utils.Mixins.models import CrmMixin, SlugifyMixin, TranslateMixin


class Post(CrmMixin, SlugifyMixin, TranslateMixin):
    TRANSLATED_FIELDS = ['title', 'description', 'text']
    SLUGIFY_FIELD = 'title'

    title_data = models.JSONField(default=dict, db_index=True)
    description_data = models.JSONField(default=dict)
    text_data = models.JSONField(default=dict)

    category = models.ForeignKey('Category.Category', on_delete=models.PROTECT)
    author = models.ForeignKey('User.User', on_delete=models.PROTECT)
    color = models.ForeignKey('Colors.PostColor', on_delete=models.PROTECT)

    by_the_creator = models.BooleanField(default=False, verbose_name='Flag that the post was created by the author')

    class Meta:
        db_table = 'post'

    def set_by_creator(self, admin=None):
        self.by_the_creator = True
        self.save()
        self.modify(admin)
        return self

    def unset_by_creator(self, admin=None):
        self.by_the_creator = False
        self.save()
        self.modify(admin)
        return self

    def __str__(self):
        return self.title

    @property
    def label(self):
        return str(self)

    def get_comments(self):
        qs = PostComment.objects.select_related('post').filter(post=self)
        return qs


class PostComment(CrmMixin, MPTTModel):
    author = models.ForeignKey('User.User', on_delete=models.PROTECT)
    post = models.ForeignKey('Post.Post', on_delete=models.PROTECT)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    content = models.CharField(max_length=512)

    removed_stamp = models.DateTimeField(db_index=True, null=True)

    tree = TreeManager()

    class Meta:
        db_table = 'post_comment'

    def __str__(self):
        if not self.is_removed:
            return self.content
        return f'[{_("Removed")}]'

    @property
    def label(self):
        return str(self)

    @property
    def is_removed(self):
        return bool(self.removed_stamp)

    def remove(self, user=None):
        self.removed_stamp = timezone.now()
        self.save()
        self.modify(user)
        return self

    def undo_remove(self, user):
        self.removed_stamp = None
        self.save()
        self.modify(user)
        return self
