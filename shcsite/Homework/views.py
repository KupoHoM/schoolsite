from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import HomeWork
from .serializers import HomeWorkSerializer, MultipleFileSerializer


class HomeWorkPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 5


class HomeWorkViewSet(ModelViewSet):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializer
    permission_classes = (DjangoModelPermissions,)
    pagination_class = HomeWorkPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'hm_discipline', 'hm_lesson', 'hm_teacher']

    @action(detail=False, methods=["POST"])
    def multiple_upload(self, request):
        multi = MultipleFileSerializer(data=request.data,
                                       context={'request': request}
                                       )
        multi.is_valid(raise_exception=True)
        title = multi.validated_data.get("title")
        hm_discipline = multi.validated_data.get("hm_discipline")
        hm_lesson = multi.validated_data.get("hm_lesson")
        hm_teacher = multi.validated_data.get("hm_teacher")
        files = multi.validated_data.get("file")
        user = multi.validated_data.get("user")

        files_list = []
        for file in files:
            files_list.append(
                HomeWork(
                    title=title,
                    file=file,
                    hm_discipline_id=hm_discipline,
                    hm_lesson_id=hm_lesson,
                    hm_teacher_id=hm_teacher,
                    user=user,
                )
            )
        if files_list:
            HomeWork.objects.bulk_create(files_list)
        return Response('Success')
