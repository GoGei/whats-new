from django.contrib import messages
from django.db import models
from django.conf import settings
from django_hosts import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from core.Utils.Access.decorators import manager_required
from core.UserFeedback.models import UserFeedback
from .forms import UserFeedbackFilterForm, UserFeedbackReplyForm
from .tables import UserFeedbackTable


@manager_required
def user_feedback_list(request):
    qs = UserFeedback.objects.all().order_by('created_stamp')
    qs = qs.annotate(
        can_be_replied_annotated=models.Case(
            models.When(status=UserFeedback.Status.COMMENTED, then=models.Value(True)),
            output_field=models.BooleanField(),
            default=models.Value(False),
        )
    )

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

    qs = user_feedback.userfeedbackreply_set.select_related('admin').all().order_by('created_stamp')
    return render(request, 'Manager/UserFeedback/user_feedback_view.html',
                  {'user_feedback': user_feedback,
                   'replies': qs})


@manager_required
def user_feedback_reply(request, user_feedback_id):
    qs = UserFeedback.objects.select_related('admin')
    user_feedback = get_object_or_404(qs, pk=user_feedback_id)

    if not user_feedback.can_be_replied:
        return redirect(reverse('manager-user-feedback-view', args=[user_feedback_id], host='manager'))

    form_body = UserFeedbackReplyForm(request.POST or None,
                                      user_feedback=user_feedback,
                                      admin=request.user)
    user_feedback.on_view_action(request.user)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-user-feedback-view', args=[user_feedback_id], host='manager'))

    if form_body.is_valid():
        reply = form_body.save()
        user_feedback.on_reply_action(reply)
        messages.success(request, _(f'User feedback {user_feedback_id} was successfully replied'))
        return redirect(reverse('manager-user-feedback-view', args=[user_feedback_id], host='manager'))

    form = {
        'body': form_body,
        'buttons': {'save': True, 'cancel': True},
        'title': _('Reply to user feedback'),
        'description': _('Please, fill in the form below to reply to user feedback'),
    }

    return render(request, 'Manager/UserFeedback/user_feedback_reply_form.html',
                  {'form': form,
                   'user_feedback': user_feedback,
                   })
