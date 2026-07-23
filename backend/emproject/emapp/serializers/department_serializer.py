from rest_framework import serializers
from ..models import Role, Department, User, Project

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"