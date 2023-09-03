from django.urls import path
from django.conf.urls import url, include

from . import views
from .AuthorRequestComments import views as comment_views

urlpatterns = [
    url(r'$', views.author_request_list, name='manager-author-request-list'),
    path(r'<uuid:author_request_id>/', views.author_request_view, name='manager-author-request-view'),
    path(r'<uuid:author_request_id>/approve/', views.author_request_approve, name='manager-author-request-approve'),
    path(r'<uuid:author_request_id>/reject/', views.author_request_reject, name='manager-author-request-reject'),
    path(r'<uuid:author_request_id>/comment/', comment_views.author_request_comment_add,
         name='manager-author-request-comment'),
    url('^comment/', include('Manager.AuthorRequest.AuthorRequestComments.urls')),
]
