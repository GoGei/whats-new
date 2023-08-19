from django.conf import settings
from django_hosts import reverse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _

from core.Utils.Access.decorators import manager_required
from core.Subscription.models import Subscription
from .forms import SubscriptionFilterForm
from .tables import SubscriptionTable


@manager_required
def subscription_list(request):
    qs = Subscription.objects.prefetch_related('categories').all().order_by('email')

    filter_form = SubscriptionFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = SubscriptionTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('Subscription filter'),
            'body': filter_form,
            'action': reverse('manager-subscription-list', host='manager')
        }
    }
    return render(request, 'Manager/Subscription/subscription_list.html',
                  {'table': table})


@manager_required
def subscription_view(request, subscription_id):
    subscription = get_object_or_404(Subscription.objects.prefetch_related('categories'), pk=subscription_id)
    return render(request, 'Manager/Subscription/subscription_view.html', {'subscription': subscription})
