from rest_framework import routers

from Manager.Api.v1.User.views import UserViewSet
from Manager.Api.v1.CategoryColor.views import CategoryColorViewSet
from Manager.Api.v1.Categories.views import CategoryViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('category-colors', CategoryColorViewSet, basename='manager-category-colors'),
router_v1.register('categories', CategoryViewSet, basename='manager-categories'),
router_v1.register('users', UserViewSet, basename='manager-users'),
urlpatterns = router_v1.urls

urlpatterns += [
]
