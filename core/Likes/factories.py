from factory import SubFactory, DjangoModelFactory
from core.User.factories import UserFactory
from core.Post.factories import PostFactory, PostCommentFactory
from core.Utils.Tests.fuzzy_fields import FuzzyBoolean
from .models import PostLike, CommentLike


class LikeAbstractFactory(DjangoModelFactory):
    is_liked = FuzzyBoolean()
    user = SubFactory(UserFactory)


class PostLikeFactory(LikeAbstractFactory):
    post = SubFactory(PostFactory)

    class Meta:
        model = PostLike


class CommentLikeFactory(LikeAbstractFactory):
    comment = SubFactory(PostCommentFactory)

    class Meta:
        model = CommentLike
