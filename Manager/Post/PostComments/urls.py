from django.urls import path

from . import views

urlpatterns = [
    path(r'<int:post_comment_id>/archive/', views.post_comment_archive, name='manager-post-comment-archive'),
    path(r'<int:post_comment_id>/restore/', views.post_comment_restore, name='manager-post-comment-restore'),
    path(r'<int:post_comment_id>/remove/', views.post_comment_remove, name='manager-post-comment-remove'),
    path(r'<int:post_comment_id>/undo-remove/', views.post_comment_undo_remove,
         name='manager-post-comment-undo-remove'),
]
