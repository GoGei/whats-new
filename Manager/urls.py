from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('urls')),
    url(r'^', include('Manager.Login.urls')),
    url(r'^', include('Manager.Home.urls')),
    url(r'^users/', include('Manager.Users.urls')),
    url(r'^admins/', include('Manager.Admins.urls')),
]

from . import test

urlpatterns += [
    url(r'test/$', test.manager_test, name='manager-test'),
]
