from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed to any user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to author of that post
        return obj.author == request.user
