from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsManager

from ..models import User, Project
from ..serializers import UserListSerializer, UserCreateSerializer, ProjectSerializer

class ManagerDashboardAPIView(APIView):

    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):

        data = {
            "message": "Welcome Manager",
            "user": request.user.username,
            "role": request.user.role.role_name
        }

        return Response(data)