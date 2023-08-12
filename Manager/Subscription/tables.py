import django_tables2 as tables
from core.User.models import User


class SubscriptionTable(tables.Table):
    email = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}}, order_by=('-email',),
                                  template_name='Manager/Subscription/subscription_table_email.html')
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/Subscription/subscription_table_actions.html')

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'email',
            'actions',
        )
        attrs = {"class": "table table-hover"}