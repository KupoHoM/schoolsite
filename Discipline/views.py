from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DisciplineSerializer
from .models import Discipline
from shcsite.permissions import DjangoCustomPermissions


class DisciplineViewSet(ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = (DjangoCustomPermissions,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    #
    # @action(detail=False, methods=["POST"])
    # def multiple_upload(self, request, *args, **kwargs):
    #     serializer = MultipleFileSerializer(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     files = serializer.validated_data.get("file")
    #     title = serializer.validated_data.get("title")
    #     user = serializer.validated_data.get("user")
    #     files_list = []
    #     for file in files:
    #         files_list.append(
    #             Discipline(file=file,
    #                        title=title,
    #                        user=user,
    #                        )
    #         )
    #     if files_list:
    #         Discipline.objects.bulk_create(files_list)
    #     return Response('Success')
