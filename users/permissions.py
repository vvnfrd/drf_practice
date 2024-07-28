from rest_framework.permissions import BasePermission


class IsNotModerator(BasePermission):

    def has_permission(self, request, view):
        if not request.user.groups.filter(name='moderator').exists():
            return True