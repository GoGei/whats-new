import django_tables2 as tables
from core.AuthorRequest.models import AuthorRequest


class AuthorRequestTable(tables.Table):
    name = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}}, order_by=('-first_name',),
                                 template_name='Manager/AuthorRequest/author_request_table_name.html')
    phone = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}},
                                  template_name='Manager/AuthorRequest/author_request_table_phone.html')
    working_experience = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}},
                                               template_name='Manager/AuthorRequest/author_request_table_working_experience.html')  # noqa
    status = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}},
                                   template_name='Manager/AuthorRequest/author_request_table_status.html')
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/AuthorRequest/author_request_table_actions.html')

    class Meta:
        model = AuthorRequest
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'name',
            'email',
            'phone',
            'working_experience',
            'status',
        )
        attrs = {"class": "table table-hover"}
