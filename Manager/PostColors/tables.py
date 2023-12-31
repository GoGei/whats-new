import django_tables2 as tables
from core.Colors.models import PostColor


class PostColorTable(tables.Table):
    is_active = tables.BooleanColumn(orderable=True, order_by=('-archived_stamp',))
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/PostColor/post_color_table_actions.html')

    class Meta:
        model = PostColor
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'name',
            'value',
            'is_active',
            'actions',
        )
        attrs = {"class": "table table-hover"}
