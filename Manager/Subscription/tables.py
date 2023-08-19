import django_tables2 as tables
from core.Subscription.models import Subscription


class SubscriptionTable(tables.Table):
    categories = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                       template_name='Manager/Subscription/subscription_table_categories.html')
    email = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}}, order_by=('-email',),
                                  template_name='Manager/Subscription/subscription_table_email.html')
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/Subscription/subscription_table_actions.html')

    class Meta:
        model = Subscription
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'categories',
            'email',
            'actions',
        )
        attrs = {"class": "table table-hover"}
