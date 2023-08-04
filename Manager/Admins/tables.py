import django_tables2 as tables
from core.User.models import User


class AdminTable(tables.Table):
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/Admins/admins_table_actions.html', )

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'is_active',
            'is_staff',
            'is_superuser',
        )
        attrs = {"class": "table table-hover"}
