from rest_framework import serializers
from ..models import Role, Department, User, Project
from .role_serializer import RoleSerializer
from .department_serializer import DepartmentSerializer

class UserListSerializer(serializers.ModelSerializer):

    role = RoleSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "employee_id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "role",
            "department",
            "created_at",
            "updated_at"
        ]



class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "employee_id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "phone",
            "role",
            "department"
        ]

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        return user