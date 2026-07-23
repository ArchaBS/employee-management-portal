from rest_framework import serializers
from ..models import Role, Department, User, Project


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"