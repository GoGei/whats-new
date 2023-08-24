from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.post_list, name='manager-post-list'),
    url(r'add/$', views.post_add, name='manager-post-add'),
    path(r'<int:post_id>/', views.post_view, name='manager-post-view'),
    path(r'<int:post_id>/edit/', views.post_edit, name='manager-post-edit'),
    path(r'<int:post_id>/archive/', views.post_archive, name='manager-post-archive'),
    path(r'<int:post_id>/restore/', views.post_restore, name='manager-post-restore'),
]
