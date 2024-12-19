from rest_framework.permissions import BasePermission

class IsAgent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'agent'
    

class IsValidator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'validator'
    
class IsSuperUser(BasePermission):
    """
    Custom permission for superuser role.
    """
    def has_permission(self, request, view):
        # Check if the user is a superuser
        return request.user.role == 'superuser'


class IsAdmin(BasePermission):
    """
    Custom permission for admin role.
    """
    def has_permission(self, request, view):
        # Admin can manage only agents, validators, and account users
        return request.user.role == 'admin'


class IsAdminOrSuperUser(BasePermission):
    """
    Custom permission that allows superusers and admins to access certain views.
    """
    def has_permission(self, request, view):
        # Check if the user is an admin or superuser
        return request.user.role in ['superuser', 'admin']