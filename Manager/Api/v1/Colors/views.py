from rest_framework import filters

from Manager.Api.base_views import AdminViewSet
from core.Colors.models import CategoryColor, PostColor
from .serializers import CategoryColorSerializer, PostColorSerializer


class CategoryColorViewSet(AdminViewSet):
    queryset = CategoryColor.objects.all().order_by('name')
    serializer_class = CategoryColorSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'value')
    ordering_fields = ('name', 'value')


class PostColorViewSet(AdminViewSet):
    queryset = PostColor.objects.all().order_by('name')
    serializer_class = PostColorSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'value')
    ordering_fields = ('name', 'value')
