from datetime import date
from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import Attendance, ActivityLog
from ..serializers import AttendanceSerializer
from ..permissions import IsManager


class AttendanceAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        if request.user.role.role_name == "Manager":
            attendance = Attendance.objects.all()
        else:
            attendance = Attendance.objects.filter(assigned_to=request.user)

        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)

    # Employee Check In

    def post(self, request):

        attendance, created = Attendance.objects.get_or_create(
            assigned_to=request.user,
            date=date.today(),
            defaults={
                "check_in": timezone.localtime().time(),
                "status": "Present"
            }
        )

        if not created:
            return Response(
                {"message": "Already checked in today."},
                status=status.HTTP_400_BAD_REQUEST
            )

        ActivityLog.objects.create(
            user=request.user,
            module="Attendance",
            action="Checked In"
        )

        serializer = AttendanceSerializer(attendance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Employee Check Out

    def patch(self, request):

        attendance = get_object_or_404(
            Attendance,
            assigned_to=request.user,
            date=date.today()
        )

        attendance.check_out = timezone.localtime().time()
        attendance.save()

        ActivityLog.objects.create(
            user=request.user,
            module="Attendance",
            action="Checked Out"
        )

        serializer = AttendanceSerializer(attendance)

        return Response(serializer.data)