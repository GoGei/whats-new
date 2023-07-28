import django_tables2 as tables
from core.User.models import User


class UserTable(tables.Table):
    name = tables.TemplateColumn(template_name='Manager/Users/users_table_name_field.html', orderable=True)
    actions = tables.TemplateColumn(template_name='Manager/Users/users_table_actions.html', orderable=False)

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'name',
            'email',
            'is_active',
        )
        attrs = {"class": "table table-hover"}
