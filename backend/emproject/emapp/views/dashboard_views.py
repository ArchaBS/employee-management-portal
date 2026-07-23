from datetime import date

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..permissions import IsManager
from ..models import User, Project, Task, Leave, Attendance


class ManagerDashboardAPIView(APIView):

    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):

        total_employees = User.objects.count()

        total_projects = Project.objects.count()

        total_tasks = Task.objects.count()

        completed_tasks = Task.objects.filter(status="Completed").count()

        pending_tasks = Task.objects.exclude(status="Completed").count()

        employees_present_today = Attendance.objects.filter(
            date=date.today(),
            status="Present"
        ).count()

        employees_on_leave_today = Leave.objects.filter(
            start_date__lte=date.today(),
            end_date__gte=date.today(),
            status="Approved"
        ).count()

        data = {
            "total_employees": total_employees,
            "total_projects": total_projects,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "employees_present_today": employees_present_today,
            "employees_on_leave_today": employees_on_leave_today,
        }

        return Response(data)