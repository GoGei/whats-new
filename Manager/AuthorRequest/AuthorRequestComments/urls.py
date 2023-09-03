from django.urls import path
from . import views

urlpatterns = [
    path(r'<uuid:comment_id>/view/', views.author_request_comment_view, name='manager-author-request-comment-view'),
    path(r'<uuid:comment_id>/edit/', views.author_request_comment_edit, name='manager-author-request-comment-edit'),
    path(r'<uuid:comment_id>/archive/', views.author_request_comment_archive,
         name='manager-author-request-comment-archive'),
    path(r'<uuid:comment_id>/restore/', views.author_request_comment_restore,
         name='manager-author-request-comment-restore'),
]
