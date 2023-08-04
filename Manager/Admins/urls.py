from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.admins_list, name='manager-admins-list'),
    path(r'<int:admin_id>/', views.admins_view, name='manager-admins-view'),
]
