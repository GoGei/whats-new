from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from Manager.Api.base_views import AdminViewSet as BaseAdminViewSet
from core.User.models import User
from .serializers import AdminSerializer


class AdminViewSet(BaseAdminViewSet):
    q = Q(is_superuser=True) | Q(is_staff=True) | Q(is_author=True)
    queryset = User.objects.filter(q).order_by('email', 'first_name', 'last_name')
    serializer_class = AdminSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    ordering_fields = ('email', 'last_name')
    filterset_fields = ('is_active', 'is_staff', 'is_superuser', 'is_author')
