from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Task, Project


class TaskAnalyticsAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_tasks = Task.objects.count()
        pending = Task.objects.filter(status="Pending").count()
        in_progress = Task.objects.filter(status="In Progress").count()
        completed = Task.objects.filter(status="Completed").count()

        if total_tasks > 0:
            completion_percentage = round((completed / total_tasks) * 100, 2)
        else:
            completion_percentage = 0

        data = {
            "total_tasks": total_tasks,
            "pending": pending,
            "in_progress": in_progress,
            "completed": completed,
            "completion_percentage": completion_percentage,
        }

        return Response(data)


class ProjectAnalyticsAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_projects = Project.objects.count()
        not_started = Project.objects.filter(status="Not Started").count()
        ongoing = Project.objects.filter(status="Ongoing").count()
        completed = Project.objects.filter(status="Completed").count()

        if total_projects > 0:
            completion_percentage = round((completed / total_projects) * 100, 2)
        else:
            completion_percentage = 0

        data = {
            "total_projects": total_projects,
            "not_started": not_started,
            "ongoing": ongoing,
            "completed": completed,
            "completion_percentage": completion_percentage,
        }

        return Response(data)