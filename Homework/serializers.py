from rest_framework import serializers
from .models import HomeWork


class HomeWorkSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # file = serializers.ListField(child=serializers.FileField())

    class Meta:
        model = HomeWork
        fields = "__all__"


class MultipleFileSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    hm_discipline = serializers.IntegerField(write_only=True)
    hm_lesson = serializers.IntegerField(write_only=True)
    hm_teacher = serializers.IntegerField(write_only=True)
    file = serializers.ListField(child=serializers.FileField())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = HomeWork
        fields = '__all__'
