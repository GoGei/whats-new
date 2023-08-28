from django.conf import settings
from django_hosts import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from core.Utils.Access.decorators import manager_required
from core.User.models import User
from .forms import AuthorFilterForm
from .tables import AuthorTable


@manager_required
def authors_list(request):
    qs = User.objects.authors().order_by('email')

    filter_form = AuthorFilterForm(request.GET, queryset=qs, request=request)
    qs = filter_form.qs

    table_body = AuthorTable(qs, request=request)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body,
        'filter': {
            'title': _('Authors filter'),
            'body': filter_form,
            'action': reverse('manager-authors-list', host='manager')
        }
    }
    return render(request, 'Manager/Authors/authors_list.html',
                  {'table': table})


@manager_required
def authors_view(request, author_id):
    author = get_object_or_404(User.objects.authors(), pk=author_id)
    return render(request, 'Manager/Authors/authors_view.html', {'author': author})


@manager_required
def authors_remove_author(request, author_id):
    author = get_object_or_404(User.objects.authors(), pk=author_id)
    author.is_author = False
    author.save()
    return redirect(reverse('manager-authors-list', host='manager'))
