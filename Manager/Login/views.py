from django.http import HttpResponseRedirect
from django_hosts import reverse
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import logout, login, authenticate
from .forms import ManagerLoginForm


def login_view(request):
    user = request.user
    if user.is_authenticated:
        if user.is_manager:
            return redirect(reverse('manager-index', host='manager'))
        else:
            return redirect(reverse('home-index', host='public'))

    initial = {'email': request.COOKIES.get('email', '')}
    form_body = ManagerLoginForm(request.POST or None, initial=initial)

    if form_body.is_valid():
        data = form_body.cleaned_data
        user = authenticate(email=data.get('email'), password=data.get('password'))

        if user:
            if user.is_active:
                login(request, user)

                remember_me = data.get('remember_me')
                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True

                if user.is_manager:
                    response = HttpResponseRedirect(reverse('manager-index', host='manager'))
                    response.set_cookie('email', user.email)
                    return response
                else:
                    return redirect(reverse('home-index', host='public'))
            else:
                form_body.add_error(None, _('User is not active! Please, contact a manager'))
        else:
            form_body.add_error(None, _('User with this email and password not found'))

    form = {
        'body': form_body,
        'buttons': {'save': True}
    }

    return render(request, 'Manager/Login/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('manager-login', host='manager'))
