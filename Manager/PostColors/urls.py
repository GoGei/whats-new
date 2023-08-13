from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.post_color_list, name='manager-post-color-list'),
    url(r'add/$', views.post_color_add, name='manager-post-color-add'),
    path(r'<int:color_id>/', views.post_color_view, name='manager-post-color-view'),
    path(r'<int:color_id>/edit/', views.post_color_edit, name='manager-post-color-edit'),
    path(r'<int:color_id>/archive/', views.post_color_archive, name='manager-post-color-archive'),
    path(r'<int:color_id>/restore/', views.post_color_restore, name='manager-post-color-restore'),

    url(r'view-fixture/$', views.post_color_view_fixture, name='manager-post-color-view-fixture'),
    url(r'load-fixture/$', views.post_color_load_fixture, name='manager-post-color-load-fixture'),
    url(r'export-to-fixture/$', views.post_color_export_to_fixture,
        name='manager-post-color-export-to-fixture'),
    url(r'load-default-fixture/$', views.post_color_load_default_fixture,
        name='manager-post-color-load-default-fixture'),
]
