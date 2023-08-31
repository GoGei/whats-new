from django_hosts import reverse
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib import messages

from core.Post.models import PostComment
from core.Utils.Access.decorators import manager_required


@manager_required
def post_comment_archive(request, post_comment_id):
    post_comment = get_object_or_404(PostComment, pk=post_comment_id)
    post_comment.archive(request.user)
    messages.success(request, _(f'Comment {post_comment.id} was successfully archived'))
    return redirect(reverse('manager-post-view', args=[post_comment.post_id], host='manager'))


@manager_required
def post_comment_restore(request, post_comment_id):
    post_comment = get_object_or_404(PostComment, pk=post_comment_id)
    post_comment.restore(request.user)
    messages.success(request, _(f'Comment {post_comment.id} was successfully restored'))
    return redirect(reverse('manager-post-view', args=[post_comment.post_id], host='manager'))


@manager_required
def post_comment_remove(request, post_comment_id):
    post_comment = get_object_or_404(PostComment, pk=post_comment_id)
    post_comment.remove(request.user)
    messages.success(request, _(f'Comment {post_comment.id} was successfully removed'))
    return redirect(reverse('manager-post-view', args=[post_comment.post_id], host='manager'))


@manager_required
def post_comment_undo_remove(request, post_comment_id):
    post_comment = get_object_or_404(PostComment, pk=post_comment_id)
    post_comment.undo_remove(request.user)
    messages.success(request, _(f'Comment {post_comment.id} was successfully restored from removed'))
    return redirect(reverse('manager-post-view', args=[post_comment.post_id], host='manager'))
