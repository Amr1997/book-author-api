from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            user = request.user
            return user.is_authenticated and user.is_author
        return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve']:
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            user = request.user
            return user.is_authenticated and user.is_author and obj.author.user == user
        return False
