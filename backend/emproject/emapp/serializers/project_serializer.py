from rest_framework import serializers
from ..models import Role, Department, User, Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"