from rest_framework.permissions import BasePermission


class IsManager(BasePermission):

    def has_permission(self, request, view):
        return request.user.role.role_name == "Manager"


class IsDeveloperLead(BasePermission):

    def has_permission(self, request, view):
        return request.user.role.role_name == "Developer Lead"


class IsTestLead(BasePermission):

    def has_permission(self, request, view):
        return request.user.role.role_name == "Test Lead"


class IsDeveloper(BasePermission):

    def has_permission(self, request, view):
        return request.user.role.role_name == "Developer"


class IsTester(BasePermission):

    def has_permission(self, request, view):
        return request.user.role.role_name == "Tester"