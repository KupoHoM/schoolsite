from rest_framework import generics, mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissions

from .models import Teachers

from .serializers import TeachersSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TeachersPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class TeachersViewSet(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    pagination_class = TeachersPagination
    permission_classes = (DjangoModelPermissions,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'discipline']


# class TeachersAPIList(mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       mixins.ListModelMixin,
#                       GenericViewSet):
#     queryset = Teachers.objects.all()
#     serializer_class = TeachersSerializer
#     # permission_classes = (IsAuthenticatedOrReadOnly,)
#     pagination_class = TeachersAPIListPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'discipline']
#
#
# class TeachersAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Teachers.objects.all()
#     serializer_class = TeachersSerializer
#     # permission_classes = (IsAuthenticated,)
#     # authentication_classes = (TokenAuthentication, )
