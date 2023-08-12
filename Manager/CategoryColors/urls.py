from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.category_color_list, name='manager-category-color-list'),
    url(r'add/$', views.category_color_add, name='manager-category-color-add'),
    path(r'<int:color_id>/', views.category_color_view, name='manager-category-color-view'),
    path(r'<int:color_id>/edit/', views.category_color_edit, name='manager-category-color-edit'),
    path(r'<int:color_id>/archive/', views.category_color_archive, name='manager-category-color-archive'),
    path(r'<int:color_id>/restore/', views.category_color_restore, name='manager-category-color-restore'),
]
