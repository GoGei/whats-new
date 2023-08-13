import json

from django.core.management import call_command
from django.http import HttpResponse
from django_hosts import reverse
from django.conf import settings
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _, ungettext_lazy
from django.contrib import messages
from rest_framework.renderers import JSONRenderer

from core.Colors.models import PostColor
from core.Colors.constants import POST_COLOR_DEFAULT_FIXTURE_PATH
from core.Utils.Access.decorators import manager_required, superuser_required
from core.Utils.Exporter.exporter import CrmMixinJSONExporter
from .forms import PostColorFilterForm, PostColorFormAdd, PostColorFormEdit, PostColorImportForm
from .tables import PostColorTable


@manager_required
def post_color_list(request):
    qs = PostColor.objects.all().order_by('name', 'value')

    filter_form = PostColorFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = PostColorTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('Post color filter'),
            'body': filter_form,
            'action': reverse('manager-post-color-list', host='manager')
        }
    }
    return render(request, 'Manager/PostColor/post_color_list.html',
                  {'table': table})


@manager_required
def post_color_view(request, color_id):
    color = get_object_or_404(PostColor, pk=color_id)
    return render(request, 'Manager/PostColor/post_color_view.html', {'color': color})


@manager_required
def post_color_add(request):
    form_body = PostColorFormAdd(request.POST or None)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-post-color-list', host='manager'))

    if form_body.is_valid():
        color = form_body.save()
        messages.success(request, _(f'Post color {color.value} was successfully created'))
        return redirect(reverse('manager-post-color-list', host='manager'))

    form = {
        'body': form_body,
        'buttons': {'save': True, 'cancel': True},
        'title': _('Add post color'),
        'description': _('Please, fill in the form below to add an color'),
    }

    return render(request, 'Manager/PostColor/post_color_add.html', {'form': form})


@manager_required
def post_color_edit(request, color_id):
    color = get_object_or_404(PostColor, pk=color_id)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-post-color-view', args=[color_id], host='manager'))

    initial = model_to_dict(color)
    form_body = PostColorFormEdit(request.POST or None, instance=color, initial=initial)
    if form_body.is_valid():
        color = form_body.save()
        messages.success(request, _(f'Post color {color.value} was successfully edited'))
        return redirect(reverse('manager-post-color-view', args=[color_id], host='manager'))

    form = {
        'body': form_body,
        'buttons': {'submit': True, 'cancel': True},
        'title': _('Edit post color'),
        'description': _('Please, fill in the form below to edit an color'),
    }

    return render(request, 'Manager/PostColor/post_color_edit.html', {'form': form,
                                                                      'color': color})


@manager_required
def post_color_archive(request, color_id):
    color = get_object_or_404(PostColor.objects.prefetch_related('post_set'), pk=color_id)

    posts = color.post_set.all()
    if posts.exists():
        messages.warning(request, ungettext_lazy('This color is used in post %s time!',
                                                 'This color is used in posts %s times!') % posts.count())
    else:
        color.archive(request.user)
        messages.success(request, _(f'Post color {color.value} was successfully archived'))
    return redirect(reverse('manager-post-color-list', host='manager'))


@manager_required
def post_color_restore(request, color_id):
    color = get_object_or_404(PostColor, pk=color_id)
    color.restore(request.user)
    messages.success(request, _(f'Post color {color.value} was successfully restored'))
    return redirect(reverse('manager-post-color-list', host='manager'))


@superuser_required
def post_color_view_fixture(request):
    with open(POST_COLOR_DEFAULT_FIXTURE_PATH, 'r') as f:
        data = json.load(f)
    return render(request, 'Manager/PostColor/post_color_view_fixture.html', {'data': data})


@superuser_required
def post_color_load_fixture(request):
    print(request.FILES)
    form_body = PostColorImportForm(request.POST or None,
                                    request.FILES or None)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-post-color-list', host='manager'))

    if form_body.is_valid():
        try:
            items, created_count = form_body.load()
            messages.success(request, _(f'Post colors {created_count} was successfully created'))
            messages.success(request, _(f'Post colors {len(items)} was successfully updated'))
            return redirect(reverse('manager-post-color-list', host='manager'))
        except ValueError as e:
            form_body.add_error('file', str(e))

    form = {
        'body': form_body,
        'buttons': {'submit': True, 'cancel': True},
        'title': _('Load post colors'),
    }

    return render(request, 'Manager/PostColor/post_color_load_fixture.html', {'form': form})


@manager_required
def post_color_export_to_fixture(request):
    data = CrmMixinJSONExporter(model=PostColor, export_fields=('name', 'value')).export()
    content = JSONRenderer().render(data)

    response = HttpResponse(content, content_type='application/json')
    filename = 'post_colors.json'
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response['Cache-Control'] = 'no-cache'
    return response


@superuser_required
def post_color_load_default_fixture(request):
    call_command('load_post_color_fixture')
    messages.success(request, _('Post colors default fixture was successfully loaded'))
    return redirect(reverse('manager-post-color-list', host='manager'))
