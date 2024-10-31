from rest_framework.permissions import IsAuthenticated

class IsChef(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.role == 'chef'