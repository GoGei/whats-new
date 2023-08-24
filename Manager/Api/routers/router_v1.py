from rest_framework import routers

from Manager.Api.v1.User.views import UserViewSet, AuthorsViewSet
from Manager.Api.v1.Colors.views import CategoryColorViewSet, PostColorViewSet
from Manager.Api.v1.Categories.views import CategoryViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('authors', AuthorsViewSet, basename='manager-authors'),
router_v1.register('category-colors', CategoryColorViewSet, basename='manager-category-colors'),
router_v1.register('categories', CategoryViewSet, basename='manager-categories'),
router_v1.register('users', UserViewSet, basename='manager-users'),
router_v1.register('post-colors', PostColorViewSet, basename='manager-post-colors'),
urlpatterns = router_v1.urls

urlpatterns += [
]
