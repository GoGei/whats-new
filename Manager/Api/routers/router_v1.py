from rest_framework import routers

from Manager.Api.v1.CategoryColor.views import CategoryColorViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('category-colors', CategoryColorViewSet, basename='manager-category-colors'),
urlpatterns = router_v1.urls

urlpatterns += [
]
