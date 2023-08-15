import django_tables2 as tables
from core.Category.models import Category


class CategoryTable(tables.Table):
    is_active = tables.BooleanColumn(orderable=True, order_by=('-archived_stamp',))
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/Category/category_table_actions.html')

    class Meta:
        model = Category
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'name',
            'position',
            'is_active',
            'actions',
        )
        attrs = {"class": "table table-hover"}
