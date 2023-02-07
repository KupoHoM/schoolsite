from rest_framework import serializers
from .models import Teachers


class TeachersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Teachers
        fields = "__all__"

