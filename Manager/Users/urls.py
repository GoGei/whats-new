from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$', views.users_list, name='manager-users-list'),
]
