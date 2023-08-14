from django.conf import settings
from django_hosts import reverse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _

from core.Utils.Access.decorators import manager_required
from core.UserFeedback.models import UserFeedback
from .forms import UserFeedbackFilterForm
from .tables import UserFeedbackTable


@manager_required
def user_feedback_list(request):
    qs = UserFeedback.objects.all().order_by('created_stamp')

    filter_form = UserFeedbackFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = UserFeedbackTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('User feedback filter'),
            'body': filter_form,
            'action': reverse('manager-user-feedback-list', host='manager')
        }
    }
    return render(request, 'Manager/UserFeedback/user_feedback_list.html',
                  {'table': table})


@manager_required
def user_feedback_view(request, user_feedback_id):
    qs = UserFeedback.objects.select_related('admin').prefetch_related('userfeedbackreply_set')
    user_feedback = get_object_or_404(qs, pk=user_feedback_id)
    user_feedback.on_view_action(request.user)
    user_feedback.refresh_from_db()
    return render(request, 'Manager/UserFeedback/user_feedback_view.html', {'user_feedback': user_feedback})
