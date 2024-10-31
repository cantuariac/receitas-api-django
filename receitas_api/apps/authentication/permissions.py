from rest_framework.permissions import BasePermission

class IsChef(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'chef'