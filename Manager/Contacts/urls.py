from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.contact_list, name='manager-contact-list'),
    url(r'add/$', views.contact_add, name='manager-contact-add'),
    path(r'<int:contact_id>/', views.contact_view, name='manager-contact-view'),
    path(r'<int:contact_id>/edit/', views.contact_edit, name='manager-contact-edit'),
    path(r'<int:contact_id>/archive/', views.contact_archive, name='manager-contact-archive'),
    path(r'<int:contact_id>/restore/', views.contact_restore, name='manager-contact-restore'),
]
