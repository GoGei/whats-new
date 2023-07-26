from django.shortcuts import render
from django.conf import settings
from core.Utils.Access.decorators import manager_required
from core.User.models import User
from .tables import UserTable


@manager_required
def users_list(request):
    qs = User.objects.users().order_by('is_active', 'id')

    table_body = UserTable(qs)
    page = request.GET.get("page", 1)
    table_body.paginate(page=page, per_page=settings.ITEMS_PER_PAGE)

    table = {
        'body': table_body
    }

    return render(request, 'Manager/Users/users_list.html',
                  {'table': table})
