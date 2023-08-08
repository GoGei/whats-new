from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.author_request_list, name='manager-author-request-list'),
    path(r'<int:author_request_id>/', views.author_request_view, name='manager-author-request-view'),
    path(r'<int:author_request_id>/approve/', views.author_request_approve, name='manager-author-request-approve'),
    path(r'<int:author_request_id>/reject/', views.author_request_reject, name='manager-author-request-reject'),
]
