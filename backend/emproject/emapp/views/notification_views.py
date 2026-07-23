from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from ..models import Notification
from ..serializers import NotificationSerializer


class NotificationAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(user=request.user)

        serializer = NotificationSerializer(notifications, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = NotificationSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationStatusAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        notification = get_object_or_404(
            Notification,
            pk=pk,
            user=request.user
        )

        notification.is_read = True
        notification.save()

        return Response(
            {"message": "Notification marked as read."},
            status=status.HTTP_200_OK
        )