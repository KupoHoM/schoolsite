from rest_framework import serializers
from .models import Lessons


class LessonsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lessons
        fields = "__all__"


class MultipleFileSerializer(serializers.ModelSerializer):
    discipline = serializers.IntegerField(write_only=True)
    file = serializers.ListField(child=serializers.FileField())
    Lesson_Teacher = serializers.IntegerField(write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lessons
        fields = '__all__'
