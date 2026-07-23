from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from ..permissions import IsManager
from ..models import Task, ActivityLog
from ..serializers import TaskSerializer, TaskStatusSerializer


class TaskAPIView(APIView):

    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):

        tasks = Task.objects.all()

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():

            task = serializer.save()

            ActivityLog.objects.create(
                user=request.user,
                module="Task",
                action=f'Created task "{task.title}"'
            )

            
            if task.assigned_to:
                ActivityLog.objects.create(
                    user=request.user,
                    module="Task",
                    action=f'Assigned task "{task.title}" to {task.assigned_to.username}'
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        task = get_object_or_404(Task, pk=pk)

        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():

            task = serializer.save()

            ActivityLog.objects.create(
                user=request.user,
                module="Task",
                action=f'Updated task "{task.title}"'
            )

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        task = get_object_or_404(Task, pk=pk)

        ActivityLog.objects.create(
            user=request.user,
            module="Task",
            action=f'Deleted task "{task.title}"'
        )

        task.delete()

        return Response(
            {"message": "Task deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )


class MyTaskAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        tasks = Task.objects.filter(assigned_to=request.user)

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)


class TaskStatusAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        task = get_object_or_404(
            Task,
            pk=pk,
            assigned_to=request.user
        )

        serializer = TaskStatusSerializer(
            task,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            task = serializer.save()

            ActivityLog.objects.create(
                user=request.user,
                module="Task",
                action=f'Changed task "{task.title}" status to {task.status}'
            )

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )