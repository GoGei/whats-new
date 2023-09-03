from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'$', views.post_list, name='manager-post-list'),
    url(r'add/$', views.post_add, name='manager-post-add'),
    path(r'<uuid:post_id>/', views.post_view, name='manager-post-view'),
    path(r'<uuid:post_id>/edit/', views.post_edit, name='manager-post-edit'),
    path(r'<uuid:post_id>/archive/', views.post_archive, name='manager-post-archive'),
    path(r'<uuid:post_id>/restore/', views.post_restore, name='manager-post-restore'),

    path(r'<uuid:post_id>/set-by-creator/', views.post_set_by_creator, name='manager-post-set-by-creator'),
    path(r'<uuid:post_id>/unset-by-creator/', views.post_unset_by_creator, name='manager-post-unset-by-creator'),

    url(r'comments/', include('Manager.Post.PostComments.urls'), name='manager-post-comment'),
]
