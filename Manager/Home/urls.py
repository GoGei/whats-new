from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$', views.manager_index, name='manager-index'),
    url(r'test/$', views.new_manager_index, name='new-manager-index'),
]
