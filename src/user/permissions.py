from rest_framework.permissions import BasePermission


class IsAuthenticatedOrServiceClient(BasePermission):
    """
    Allows access only to authenticated users or service clients.
    """

    def has_permission(self, request, view):
        if request.user:
            return request.user.is_authenticated
        else:
            return True
