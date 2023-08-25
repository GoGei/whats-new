from django_hosts import reverse
from django.conf import settings
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.contrib import messages

from core.Post.models import Post
from core.Utils.Access.decorators import manager_required
from .forms import PostFilterForm, PostFormAdd, PostFormEdit
from .tables import PostTable

Queryset = Post.objects.select_related('category', 'author', 'color')


@manager_required
def post_list(request):
    qs = Queryset.all().order_by('title_data')

    filter_form = PostFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = PostTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('Post filter'),
            'body': filter_form,
            'action': reverse('manager-post-list', host='manager')
        }
    }
    return render(request, 'Manager/Post/post_list.html',
                  {'table': table})


@manager_required
def post_view(request, post_id):
    post = get_object_or_404(Queryset, pk=post_id)
    return render(request, 'Manager/Post/post_view.html', {'post': post})


@manager_required
def post_add(request):
    form_body = PostFormAdd(request.POST or None)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-post-list', host='manager'))

    if form_body.is_valid():
        post = form_body.save()
        messages.success(request, _(f'Post {post.title} was successfully created'))
        return redirect(reverse('manager-post-list', host='manager'))

    form = {
        'body': form_body,
        'buttons': {'save': True, 'cancel': True},
        'title': _('Add post'),
        'description': _('Please, fill in the form below to add a post'),
    }

    return render(request, 'Manager/Post/post_add.html', {'form': form})


@manager_required
def post_edit(request, post_id):
    post = get_object_or_404(Queryset, pk=post_id)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-post-view', args=[post_id], host='manager'))

    initial = model_to_dict(post)
    form_body = PostFormEdit(request.POST or None, instance=post, initial=initial)
    if form_body.is_valid():
        post = form_body.save()
        messages.success(request, _(f'Post {post.title} was successfully edited'))
        return redirect(reverse('manager-post-view', args=[post_id], host='manager'))

    form = {
        'body': form_body,
        'buttons': {'submit': True, 'cancel': True},
        'title': _('Edit post'),
        'description': _('Please, fill in the form below to edit a post'),
    }

    return render(request, 'Manager/Post/post_edit.html', {'form': form,
                                                           'post': post})


@manager_required
def post_archive(request, post_id):
    post = get_object_or_404(Queryset, pk=post_id)
    post.archive(request.user)
    messages.success(request, _(f'Post {post.title} was successfully archived'))
    return redirect(reverse('manager-post-list', host='manager'))


@manager_required
def post_restore(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.restore(request.user)
    messages.success(request, _(f'Post {post.title} was successfully restored'))
    return redirect(reverse('manager-post-list', host='manager'))


@manager_required
def post_set_by_creator(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.set_by_creator(request.user)
    messages.success(request, _(f'Post {post.title} was successfully set "By creator" flag'))
    return redirect(reverse('manager-post-list', host='manager'))


@manager_required
def post_unset_by_creator(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.unset_by_creator(request.user)
    messages.success(request, _(f'Post {post.title} was successfully unset "By creator" flag'))
    return redirect(reverse('manager-post-list', host='manager'))
