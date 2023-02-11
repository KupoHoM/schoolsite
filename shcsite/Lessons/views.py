from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Lessons
from .serializers import LessonsSerializer, MultipleFileSerializer
from shcsite.permissions import DjangoCustomPermissions


class LessonsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class LessonsViewSet(ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (DjangoCustomPermissions,)
    pagination_class = LessonsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'discipline', 'Lesson_Teacher', ]

    @action(detail=False, methods=["POST"])
    def multiple_upload(self, request, *args, **kwargs):
        multi = MultipleFileSerializer(data=request.data,
                                       context={'request': request}
                                       )
        multi.is_valid(raise_exception=True)
        title = multi.validated_data.get("title")
        content = multi.validated_data.get("content")
        files = multi.validated_data.get("file")
        is_published = multi.validated_data.get("is_published")
        discipline = multi.validated_data.get("discipline")
        lesson_teacher = multi.validated_data.get("Lesson_Teacher")
        user = multi.validated_data.get("user")

        files_list = []
        for file in files:
            files_list.append(
                Lessons(
                    title=title,
                    content=content,
                    file=file,
                    is_published=is_published,
                    Lesson_Teacher_id=lesson_teacher,
                    discipline_id=discipline,
                    user=user,
                )
            )
        if files_list:
            Lessons.objects.bulk_create(files_list)
        return Response('Success')
