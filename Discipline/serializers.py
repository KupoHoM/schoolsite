from rest_framework import serializers, request
from .models import Discipline


class DisciplineSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Discipline
        fields = "__all__"

# class MultipleFileSerializer(serializers.HyperlinkedModelSerializer):
#     title = serializers.CharField()
#     file = serializers.ListField(
#         child=serializers.FileField()
#     )
#
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Discipline
#         fields = "__all__"
