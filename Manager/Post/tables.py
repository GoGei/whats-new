import django_tables2 as tables
from core.Post.models import Post


class PostTable(tables.Table):
    title = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}}, order_by=('-title_data',),
                                  template_name='Manager/Post/post_table_title.html')
    category = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}},
                                     order_by=('-category__name_data',),
                                     template_name='Manager/Post/post_table_category.html')
    author = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}}, order_by=('-author__email',),
                                   template_name='Manager/Post/post_table_author.html')
    color = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}}, order_by=('-color__name',),
                                  template_name='Manager/Post/post_table_color.html')
    is_active = tables.BooleanColumn(orderable=True, order_by=('-archived_stamp',))
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/Post/post_table_actions.html')

    class Meta:
        model = Post
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'title',
            'category',
            'author',
            'color',
            'is_active',
            'actions',
        )
        attrs = {"class": "table table-hover"}
