from rest_framework import serializers
from .models import ProjectTool


class ProjectToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTool
        fields = "__all__"
