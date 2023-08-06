from django.db import models
from core.Utils.Mixins.models import CrmMixin


class LikeAbstract(CrmMixin):
    is_liked = models.BooleanField(default=None, db_index=True, null=True)
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def like(self):
        self.is_liked = True
        self.save()
        return self

    def dislike(self):
        self.is_liked = False
        self.save()
        return self

    def deactivate(self):
        self.is_liked = None
        self.save()
        return self


class PostLike(LikeAbstract):
    post = models.ForeignKey('Post.Post', on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_like'


class CommentLike(LikeAbstract):
    comment = models.ForeignKey('Post.PostComment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment_like'
