from django.conf import settings
from django_hosts import reverse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _

from core.Utils.Access.decorators import manager_required
from core.User.models import User
from .forms import AdminFilterForm
from .tables import AdminTable


@manager_required
def admins_list(request):
    qs = User.objects.admins().order_by('email')

    filter_form = AdminFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = AdminTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('Admin filter'),
            'body': filter_form,
            'action': reverse('manager-admins-list', host='manager')
        }
    }
    return render(request, 'Manager/Admins/admins_list.html',
                  {'table': table})


@manager_required
def admins_view(request, admin_id):
    admin = get_object_or_404(User, pk=admin_id)
    return render(request, 'Manager/Admins/admins_view.html', {'admin': admin})
