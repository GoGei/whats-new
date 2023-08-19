from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.category_list, name='manager-category-list'),
    url(r'add/$', views.category_add, name='manager-category-add'),
    path(r'<int:category_id>/', views.category_view, name='manager-category-view'),
    path(r'<int:category_id>/edit/', views.category_edit, name='manager-category-edit'),
    path(r'<int:category_id>/archive/', views.category_archive, name='manager-category-archive'),
    path(r'<int:category_id>/restore/', views.category_restore, name='manager-category-restore'),
]
