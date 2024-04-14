from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (
                request.user
                and request.user.is_staff
                and request.method != "DELETE"
                )
        )


class IsAuthenticatedListAndCreate(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in ("GET", "CREATE")
            and request.user
            and request.user.is_authenticated
        )
