from django.conf import settings
from django.forms import model_to_dict
from django_hosts import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _, ungettext_lazy
from django.contrib import messages

from core.Utils.Access.decorators import manager_required, superuser_required
from core.Colors.models import CategoryColor
from .forms import CategoryColorFilterForm, CategoryColorFormAdd, CategoryColorFormEdit
from .tables import CategoryColorTable


@manager_required
def category_color_list(request):
    qs = CategoryColor.objects.all().order_by('name', 'value')

    filter_form = CategoryColorFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = CategoryColorTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('Category color filter'),
            'body': filter_form,
            'action': reverse('manager-category-color-list', host='manager')
        }
    }
    return render(request, 'Manager/CategoryColor/category_color_list.html',
                  {'table': table})


@manager_required
def category_color_view(request, color_id):
    color = get_object_or_404(CategoryColor, pk=color_id)
    return render(request, 'Manager/CategoryColor/category_color_view.html', {'color': color})


@superuser_required
def category_color_add(request):
    form_body = CategoryColorFormAdd(request.POST or None)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-category-color-list', host='manager'))

    if form_body.is_valid():
        color = form_body.save()
        messages.success(request, _(f'Category color {color.value} was successfully created'))
        return redirect(reverse('manager-category-color-list', host='manager'))

    form = {
        'body': form_body,
        'buttons': {'save': True, 'cancel': True},
        'title': _('Add color'),
        'description': _('Please, fill in the form below to add an color'),
    }

    return render(request, 'Manager/CategoryColor/category_color_add.html', {'form': form})


@superuser_required
def category_color_edit(request, color_id):
    color = get_object_or_404(CategoryColor, pk=color_id)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-category-color-view', args=[color_id], host='manager'))

    initial = model_to_dict(color)
    form_body = CategoryColorFormEdit(request.POST or None, instance=color, initial=initial)
    if form_body.is_valid():
        color = form_body.save()
        messages.success(request, _(f'Category color {color.value} was successfully edited'))
        return redirect(reverse('manager-category-color-view', args=[color_id], host='manager'))

    form = {
        'body': form_body,
        'buttons': {'submit': True, 'cancel': True},
        'title': _('Edit category color'),
        'description': _('Please, fill in the form below to edit an color'),
    }

    return render(request, 'Manager/CategoryColor/category_color_edit.html', {'form': form,
                                                                              'color': color})


@manager_required
def category_color_archive(request, color_id):
    color = get_object_or_404(CategoryColor.objects.prefetch_related('category_set'), pk=color_id)

    categories = color.category_set.all()
    if categories.exists():
        messages.warning(request, ungettext_lazy('This color is used in category %s time!',
                                                 'This color is used in categories %s times!') % categories.count())
    else:
        color.archive(request.user)
        messages.success(request, _(f'Category color {color.value} was successfully archived'))
    return redirect(reverse('manager-category-color-list', host='manager'))


@manager_required
def category_color_restore(request, color_id):
    color = get_object_or_404(CategoryColor, pk=color_id)
    color.restore(request.user)
    messages.success(request, _(f'Category color {color.value} was successfully restored'))
    return redirect(reverse('manager-category-color-list', host='manager'))
