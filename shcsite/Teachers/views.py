from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Teachers
from .serializers import TeachersSerializer
from shcsite.permissions import DjangoCustomPermissions


class TeachersPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 2


class TeachersViewSet(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    pagination_class = TeachersPagination
    permission_classes = (DjangoCustomPermissions,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'discipline']
