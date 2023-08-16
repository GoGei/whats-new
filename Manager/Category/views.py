from django_hosts import reverse
from django.conf import settings
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _, ungettext_lazy
from django.contrib import messages

from core.Category.models import Category
from core.Utils.Access.decorators import manager_required
from .forms import CategoryFilterForm, CategoryFormAdd, CategoryFormEdit
from .tables import CategoryTable


@manager_required
def category_list(request):
    qs = Category.objects.select_related('color').all().order_by('position', 'name_data')

    filter_form = CategoryFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = CategoryTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('Category filter'),
            'body': filter_form,
            'action': reverse('manager-category-list', host='manager')
        }
    }
    return render(request, 'Manager/Category/category_list.html',
                  {'table': table})


@manager_required
def category_view(request, category_id):
    category = get_object_or_404(Category.objects.select_related('color').prefetch_related('post_set'), pk=category_id)
    return render(request, 'Manager/Category/category_view.html', {'category': category})


@manager_required
def category_add(request):
    form_body = CategoryFormAdd(request.POST or None)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-category-list', host='manager'))

    if form_body.is_valid():
        category = form_body.save()
        messages.success(request, _(f'Category {category.name} was successfully created'))
        return redirect(reverse('manager-category-list', host='manager'))

    form = {
        'body': form_body,
        'buttons': {'save': True, 'cancel': True},
        'title': _('Add category'),
        'description': _('Please, fill in the form below to add a category'),
    }

    return render(request, 'Manager/Category/category_add.html', {'form': form})


@manager_required
def category_edit(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if '_cancel' in request.POST:
        return redirect(reverse('manager-category-view', args=[category_id], host='manager'))

    initial = model_to_dict(category)
    form_body = CategoryFormEdit(request.POST or None, instance=category, initial=initial)
    if form_body.is_valid():
        category = form_body.save()
        messages.success(request, _(f'Category category {category.name} was successfully edited'))
        return redirect(reverse('manager-category-view', args=[category_id], host='manager'))

    form = {
        'body': form_body,
        'buttons': {'submit': True, 'cancel': True},
        'title': _('Edit category'),
        'description': _('Please, fill in the form below to edit a category'),
    }

    return render(request, 'Manager/Category/category_edit.html', {'form': form,
                                                                   'category': category})


@manager_required
def category_archive(request, category_id):
    category = get_object_or_404(Category.objects.prefetch_related('post_set'), pk=category_id)

    posts = category.post_set.all()
    if posts.exists():
        messages.warning(request, ungettext_lazy('This category is used in post %s time!',
                                                 'This category is used in posts %s times!') % posts.count())
    else:
        category.archive(request.user)
        messages.success(request, _(f'Category {category.name} was successfully archived'))
    return redirect(reverse('manager-category-list', host='manager'))


@manager_required
def category_restore(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.restore(request.user)
    messages.success(request, _(f'Category category {category.name} was successfully restored'))
    return redirect(reverse('manager-category-list', host='manager'))
