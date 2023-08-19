from django.conf import settings
from django_hosts import reverse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from core.Utils.Access.decorators import manager_required
from core.AuthorRequest.models import AuthorRequest, AuthorRequestComment
from .forms import AuthorRequestFilterForm
from .tables import AuthorRequestTable
from .AuthorRequestComments.forms import AuthorRequestCommentFilterForm
from .AuthorRequestComments.tables import AuthorRequestCommentTable


@manager_required
def author_request_list(request):
    qs = AuthorRequest.objects.all().order_by('email')

    filter_form = AuthorRequestFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = AuthorRequestTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('Author request filter'),
            'body': filter_form,
            'action': reverse('manager-author-request-list', host='manager')
        }
    }
    return render(request, 'Manager/AuthorRequest/author_request_list.html',
                  {'table': table})


@manager_required
def author_request_view(request, author_request_id):
    author_request = get_object_or_404(AuthorRequest, pk=author_request_id)

    qs = AuthorRequestComment.objects.select_related('author_request', 'user')
    qs = qs.filter(author_request=author_request).order_by('created_stamp')

    filter_form = AuthorRequestCommentFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = AuthorRequestCommentTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'skips': {'table_no_data': True},
        # 'filter': {
        #     'title': _('Comments filter'),
        #     'body': filter_form,
        #     'action': reverse('manager-author-request-view', args=[author_request_id], host='manager')
        # }
    }
    return render(request, 'Manager/AuthorRequest/author_request_view.html',
                  {'author_request': author_request,
                   'table': table})


@manager_required
def author_request_approve(request, author_request_id):
    author_request = get_object_or_404(AuthorRequest, pk=author_request_id)
    author_request.approve(request.user)
    messages.success(request, _(f'Request {author_request_id} was successfully approved'))
    return redirect(reverse('manager-author-request-list', host='manager'))


@manager_required
def author_request_reject(request, author_request_id):
    author_request = get_object_or_404(AuthorRequest, pk=author_request_id)
    author_request.reject(request.user)
    messages.success(request, _(f'Request {author_request_id} was successfully rejected'))
    return redirect(reverse('manager-author-request-list', host='manager'))
