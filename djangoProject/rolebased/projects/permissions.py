from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsWorkerOrReadOnly(BasePermission):
    """
    Workers: can create, update, delete projects
    Admins: can only read projects
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role == "worker":
            return True
        if request.user.role == "admin":
            return request.method in SAFE_METHODS  # Only GET, HEAD, OPTIONS
        return False
