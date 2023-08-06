from unittest.mock import patch, PropertyMock

from django.test import TestCase

from ..models import AuthorRequestComment
from ..factories import AuthorRequestCommentFactory


class AuthorRequestCommentTests(TestCase):
    def test_create(self):
        obj = AuthorRequestCommentFactory.create()
        qs = AuthorRequestComment.objects.filter(pk=obj.pk)
        self.assertTrue(qs.exists())
        self.assertEqual(qs[0], obj)

    def test_delete(self):
        obj = AuthorRequestCommentFactory.create()
        obj.delete()

        qs = AuthorRequestComment.objects.filter(pk=obj.pk)
        self.assertFalse(qs.exists())

    def test_str(self):
        obj = AuthorRequestCommentFactory.create()
        lim = AuthorRequestComment.COMMENT_STR_LIMIT
        self.assertTrue(obj.comment[:lim - 5] in str(obj))
        self.assertTrue(obj.comment[:lim - 5] in obj.label)

        lim = 10
        with patch.object(AuthorRequestComment, 'COMMENT_STR_LIMIT', new_callable=PropertyMock(return_value=lim)), \
                patch.object(AuthorRequestComment, 'END_COMMENT', new_callable=PropertyMock(return_value='...')):
            comment = '1324567890'
            obj = AuthorRequestCommentFactory.create(comment=comment)
            expected = '1324567890'
            self.assertEqual(expected, str(obj))
            self.assertEqual(expected, obj.label)

            comment = '1324567890' * 2
            obj = AuthorRequestCommentFactory.create(comment=comment)
            expected = '1324567...'
            self.assertEqual(expected, str(obj))
            self.assertEqual(expected, obj.label)
