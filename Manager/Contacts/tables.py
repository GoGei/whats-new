import django_tables2 as tables
from core.Contacts.models import Contacts


class ContactsTable(tables.Table):
    text = tables.TemplateColumn(orderable=True, attrs={"td": {"style": "width: 15%"}},
                                 extra_context={'contact_types': Contacts.ContactType},
                                 template_name='Manager/Contacts/contact_table_text.html')
    is_active = tables.BooleanColumn(orderable=True, order_by=('-archived_stamp',))
    actions = tables.TemplateColumn(orderable=False, attrs={"td": {"style": "width: 15%"}},
                                    template_name='Manager/Contacts/contact_table_actions.html')

    class Meta:
        model = Contacts
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'text',
            'contact_type',
            'icon',
            'is_active',
            'actions',
        )
        attrs = {"class": "table table-hover"}
