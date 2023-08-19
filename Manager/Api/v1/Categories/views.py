from rest_framework import filters

from Manager.Api.base_views import AdminViewSet
from core.Category.models import Category
from .serializers import CategorySerializer


class CategoryViewSet(AdminViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name_data', 'slug')
    ordering_fields = ('name', 'position')
