from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.user_feedback_list, name='manager-user-feedback-list'),
    path(r'<int:user_feedback_id>/', views.user_feedback_view, name='manager-user-feedback-view'),
]
