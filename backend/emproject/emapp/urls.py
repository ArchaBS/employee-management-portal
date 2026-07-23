from django.urls import path
from .views import (
    UserListAPIView,
    ManagerDashboardAPIView,
    ProjectAPIView,
    TaskAPIView,
    MyTaskAPIView,
    TaskStatusAPIView,
    LeaveAPIView,
    AttendanceAPIView,
    NotificationAPIView,
    NotificationStatusAPIView,
    ReportsAPIView,
    TaskAnalyticsAPIView,
    ProjectAnalyticsAPIView,
    ActivityLogAPIView,
)

urlpatterns = [

    path("users/", UserListAPIView.as_view(), name="users"),

    path("users/<int:pk>/",UserListAPIView.as_view(),name="user-detail"),

    path('dashboard/manager/',ManagerDashboardAPIView.as_view(),name='manager-dashboard'),

    path("projects/", ProjectAPIView.as_view(), name="project-api"),

    path("tasks/", TaskAPIView.as_view(), name="task-api"),

    path("tasks/<int:pk>/",TaskAPIView.as_view(),name="task-detail"),

    path("tasks/my/", MyTaskAPIView.as_view(), name="my-tasks"),

    path("tasks/status/<int:pk>/",TaskStatusAPIView.as_view(),name="task-status",),

    path("leaves/", LeaveAPIView.as_view(), name="leave-api"),
    path("leaves/<int:pk>/", LeaveAPIView.as_view(), name="leave-detail"),

    path("attendance/", AttendanceAPIView.as_view(), name="attendance"),

    path("dashboard/manager/",ManagerDashboardAPIView.as_view(),name="manager-dashboard"),

    path("notifications/", NotificationAPIView.as_view(), name="notification-api"),
    path("notifications/<int:pk>/", NotificationStatusAPIView.as_view(), name="notification-status"),

    path("reports/", ReportsAPIView.as_view(), name="reports"),

    path("analytics/tasks/", TaskAnalyticsAPIView.as_view(), name="task-analytics"),
    path("analytics/projects/", ProjectAnalyticsAPIView.as_view(), name="project-analytics"),

    path("activity/",ActivityLogAPIView.as_view(),name="activity-log",),

]