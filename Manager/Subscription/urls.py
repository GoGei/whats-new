from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.subscription_list, name='manager-subscription-list'),
    path(r'<uuid:subscription_id>/', views.subscription_view, name='manager-subscription-view'),
]
