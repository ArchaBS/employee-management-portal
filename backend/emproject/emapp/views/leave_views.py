from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from ..permissions import IsManager
from ..models import Leave, ActivityLog
from ..serializers import LeaveSerializer


class LeaveAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        leaves = Leave.objects.all()

        serializer = LeaveSerializer(leaves, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = LeaveSerializer(data=request.data)

        if serializer.is_valid():

            leave = serializer.save()

            ActivityLog.objects.create(
                user=request.user,
                module="Leave",
                action="Applied for leave"
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        leave = get_object_or_404(Leave, pk=pk)

        serializer = LeaveSerializer(leave, data=request.data)

        if serializer.is_valid():

            leave = serializer.save()

            ActivityLog.objects.create(
                user=request.user,
                module="Leave",
                action=f'Updated leave request ({leave.status})'
            )

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)