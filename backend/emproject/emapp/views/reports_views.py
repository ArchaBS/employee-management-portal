from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsManager
from ..models import User, Project, Task, Leave, Attendance


class ReportsAPIView(APIView):

    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):

        data = {
            "total_employees": User.objects.count(),
            "total_projects": Project.objects.count(),
            "total_tasks": Task.objects.count(),
            "completed_tasks": Task.objects.filter(status="Completed").count(),
            "pending_tasks": Task.objects.filter(status="Pending").count(),
            "approved_leaves": Leave.objects.filter(status="Approved").count(),
            "present_today": Attendance.objects.filter(status="Present").count(),
        }

        return Response(data)