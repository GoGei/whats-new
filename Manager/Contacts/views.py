from django_hosts import reverse
from django.conf import settings
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib import messages

from core.Contacts.models import Contacts
from core.Utils.Access.decorators import manager_required
from .forms import ContactsFilterForm, ContactsFormAdd, ContactsFormEdit
from .tables import ContactsTable


@manager_required
def contact_list(request):
    qs = Contacts.objects.all().order_by('text', 'contact_type')

    filter_form = ContactsFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = ContactsTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('Contact filter'),
            'body': filter_form,
            'action': reverse('manager-contact-list', host='manager')
        }
    }
    return render(request, 'Manager/Contacts/contact_list.html',
                  {'table': table})


@manager_required
def contact_view(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id)
    contact_types = Contacts.ContactType
    return render(request, 'Manager/Contacts/contact_view.html', {'contact': contact,
                                                                  'contact_types': contact_types})


@manager_required
def contact_add(request):
    form_body = ContactsFormAdd(request.POST or None,
                                request.FILES or None)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-contact-list', host='manager'))

    if form_body.is_valid():
        contact = form_body.save()
        messages.success(request, _(f'Contact {contact.id} was successfully created'))
        return redirect(reverse('manager-contact-list', host='manager'))

    form = {
        'body': form_body,
        'buttons': {'save': True, 'cancel': True},
        'title': _('Add contact'),
        'description': _('Please, fill in the form below to add an contact'),
    }

    return render(request, 'Manager/Contacts/contact_add.html', {'form': form})


@manager_required
def contact_edit(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-contact-view', args=[contact_id], host='manager'))

    initial = model_to_dict(contact)
    form_body = ContactsFormEdit(request.POST or None,
                                 request.FILES or None,
                                 instance=contact, initial=initial)
    if form_body.is_valid():
        contact = form_body.save()
        messages.success(request, _(f'Contact {contact.id} was successfully edited'))
        return redirect(reverse('manager-contact-view', args=[contact_id], host='manager'))

    form = {
        'body': form_body,
        'buttons': {'submit': True, 'cancel': True},
        'title': _('Edit contact'),
        'description': _('Please, fill in the form below to edit an contact'),
    }

    return render(request, 'Manager/Contacts/contact_edit.html', {'form': form,
                                                                  'contact': contact})


@manager_required
def contact_archive(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id)
    contact.archive(request.user)
    messages.success(request, _(f'Contact {contact.id} was successfully archived'))
    return redirect(reverse('manager-contact-list', host='manager'))


@manager_required
def contact_restore(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id)
    contact.restore(request.user)
    messages.success(request, _(f'Contact {contact.id} was successfully restored'))
    return redirect(reverse('manager-contact-list', host='manager'))
