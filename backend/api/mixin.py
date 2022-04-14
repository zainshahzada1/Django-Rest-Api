from .permissions import IsStaffEditorPermissions
from rest_framework import permissions

class IsStaffEditorPermissionsMixin():
    permission_classes=[permissions.IsAdminUser,IsStaffEditorPermissions]