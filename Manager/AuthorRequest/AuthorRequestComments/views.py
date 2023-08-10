from django.forms import model_to_dict
from django_hosts import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib import messages

from core.Utils.Access.decorators import manager_required, superuser_required
from core.AuthorRequest.models import AuthorRequestComment, AuthorRequest
from .forms import AuthorRequestCommentFormAdd, AuthorRequestCommentFormEdit


def get_qs():
    return AuthorRequestComment.objects.select_related('author_request')


@manager_required
def author_request_comment_view(request, comment_id):
    comment = get_object_or_404(get_qs(), pk=comment_id)
    return render(request, 'Manager/AuthorRequest/AuthorRequestComment/author_request_comment_view.html',
                  {'comment': comment,
                   'author_request': comment.author_request})


@superuser_required
def author_request_comment_add(request, author_request_id):
    author_request = get_object_or_404(AuthorRequest, pk=author_request_id)
    form_body = AuthorRequestCommentFormAdd(request.POST or None,
                                            author_request=author_request,
                                            user=request.user)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-author-request-view', args=[author_request_id], host='manager'))

    if form_body.is_valid():
        form_body.save()
        messages.success(request, _(f'Author request {author_request_id} was successfully commented'))
        return redirect(reverse('manager-author-request-view', args=[author_request_id], host='manager'))

    form = {
        'body': form_body,
        'buttons': {'save': True, 'cancel': True},
        'title': _('Add comment'),
        'description': _('Please, fill in the form below to add an comment'),
    }

    return render(request,
                  'Manager/AuthorRequest/AuthorRequestComment/author_request_comment_add.html',
                  {'form': form,
                   'author_request': author_request})


@superuser_required
def author_request_comment_edit(request, comment_id):
    comment = get_object_or_404(get_qs(), pk=comment_id)

    if not comment.is_author(request.user):
        messages.warning(request, _(f'Comment {comment.id} is not yours. Only author can interact with it'))
        return redirect(reverse('manager-author-request-view', args=[comment.author_request_id], host='manager'))

    if '_cancel' in request.POST:
        return redirect(reverse('manager-author-request-view', args=[comment.author_request_id], host='manager'))

    initial = model_to_dict(comment)
    form_body = AuthorRequestCommentFormEdit(request.POST or None, instance=comment, initial=initial)
    if form_body.is_valid():
        comment = form_body.save()
        messages.success(request, _(f'Comment {comment.id} was successfully edited'))
        return redirect(reverse('manager-author-request-view', args=[comment.author_request_id], host='manager'))

    form = {
        'body': form_body,
        'buttons': {'submit': True, 'cancel': True},
        'title': _('Edit comment'),
        'description': _('Please, fill in the form below to edit an comment'),
    }

    return render(request,
                  'Manager/AuthorRequest/AuthorRequestComment/author_request_comment_edit.html',
                  {'form': form,
                   'comment': comment,
                   'author_request': comment.author_request})


@manager_required
def author_request_comment_archive(request, comment_id):
    comment = get_object_or_404(get_qs(), pk=comment_id)
    if comment.is_author(request.user):
        comment.archive(request.user)
        messages.success(request, _(f'Comment {comment.id} was successfully archived'))
    else:
        messages.warning(request, _(f'Comment {comment.id} is not yours. Only author can interact with it'))
    return redirect(reverse('manager-author-request-view', args=[comment.author_request_id], host='manager'))


@manager_required
def author_request_comment_restore(request, comment_id):
    comment = get_object_or_404(get_qs(), pk=comment_id)
    if comment.is_author(request.user):
        comment.restore(request.user)
        messages.success(request, _(f'Comment {comment.id} was successfully restored'))
    else:
        messages.warning(request, _(f'Comment {comment.id} is not yours. Only author can interact with it'))
    return redirect(reverse('manager-author-request-view', args=[comment.author_request_id], host='manager'))
