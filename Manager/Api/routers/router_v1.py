from rest_framework import routers

from Manager.Api.v1.User.views import AdminViewSet
from Manager.Api.v1.CategoryColor.views import CategoryColorViewSet
from Manager.Api.v1.Categories.views import CategoryViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('admins', AdminViewSet, basename='manager-admins'),
router_v1.register('category-colors', CategoryColorViewSet, basename='manager-category-colors'),
router_v1.register('categories', CategoryViewSet, basename='manager-categories'),
urlpatterns = router_v1.urls

urlpatterns += [
]
