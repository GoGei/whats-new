from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$', views.users_list, name='manager-users-list'),
    url(r'<int:user_id>$', views.users_view, name='manager-users-view'),
]
