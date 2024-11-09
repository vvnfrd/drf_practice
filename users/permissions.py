from rest_framework.permissions import BasePermission


class IsNotModerator(BasePermission):

    def has_permission(self, request, view):
        if not request.user.groups.filter(name='moderator').exists():
            return True

class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True

class IsOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().author

class IsSubscriber(BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().user