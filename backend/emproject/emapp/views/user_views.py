from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsManager
from ..models import User, Project, ActivityLog
from ..serializers import (
    UserListSerializer,
    UserCreateSerializer,
    ProjectSerializer,
)


class UserListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        users = User.objects.all()

        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            ActivityLog.objects.create(
                user=request.user,
                module="User",
                action=f'Created employee "{user.username}"'
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        user = get_object_or_404(User, pk=pk)

        serializer = UserCreateSerializer(
            user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            user = serializer.save()

            ActivityLog.objects.create(
                user=request.user,
                module="User",
                action=f'Updated employee "{user.username}"'
            )

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        user = get_object_or_404(User, pk=pk)

        username = user.username

        ActivityLog.objects.create(
            user=request.user,
            module="User",
            action=f'Deleted employee "{username}"'
        )

        user.delete()

        return Response(
            {"message": "Employee deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )