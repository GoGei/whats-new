import django_tables2 as tables
from core.UserFeedback.models import UserFeedback


class UserFeedbackTable(tables.Table):
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/UserFeedback/user_feedback_table_actions.html')

    class Meta:
        model = UserFeedback
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'created_stamp',
            'status',
            'actions',
        )
        attrs = {"class": "table table-hover"}
