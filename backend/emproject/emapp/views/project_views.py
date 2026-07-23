from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from ..models import Project, ActivityLog
from ..serializers import ProjectSerializer
from ..permissions import IsManager


class ProjectAPIView(APIView):

    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):

        projects = Project.objects.all()

        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():

            project = serializer.save()

            ActivityLog.objects.create(
                user=request.user,
                module="Project",
                action=f'Created project "{project.project_name}"'
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk):

        project = get_object_or_404(Project, pk=pk)

        serializer = ProjectSerializer(
            project,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            ActivityLog.objects.create(
                user=request.user,
                module="Project",
                action=f'Updated project "{project.project_name}"'
            )

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        project = get_object_or_404(Project, pk=pk)

        ActivityLog.objects.create(
            user=request.user,
            module="Project",
            action=f'Deleted project "{project.project_name}"'
        )

        project.delete()

        return Response(
            {"message": "Project deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )