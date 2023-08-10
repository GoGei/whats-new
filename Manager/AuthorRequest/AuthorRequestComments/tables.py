import django_tables2 as tables
from core.AuthorRequest.models import AuthorRequestComment


class AuthorRequestCommentTable(tables.Table):
    comment = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/AuthorRequest/AuthorRequestComment/author_request_comment_table_comment.html')  # noqa
    user = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}}, order_by=('user__email',),
                                 template_name='Manager/AuthorRequest/AuthorRequestComment/author_request_comment_table_user.html')  # noqa
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/AuthorRequest/AuthorRequestComment/author_request_comment_table_actions.html')  # noqa

    class Meta:
        model = AuthorRequestComment
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'comment',
            'user',
            'actions',
        )
        attrs = {"class": "table table-hover"}
