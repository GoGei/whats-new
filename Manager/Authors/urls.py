from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.authors_list, name='manager-authors-list'),
    path(r'<int:author_id>/', views.authors_view, name='manager-authors-view'),
    path(r'<int:author_id>/remove-author/', views.authors_remove_author, name='manager-authors-remove-author'),
]
