from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import ActivityLog
from ..serializers import ActivityLogSerializer
from ..permissions import IsManager


class ActivityLogAPIView(APIView):

    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):

        activities = ActivityLog.objects.all()

        serializer = ActivityLogSerializer(
            activities,
            many=True
        )

        return Response(serializer.data)