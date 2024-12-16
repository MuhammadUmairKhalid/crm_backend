from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from .models import User, Form, Company


class CustomUserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'role', 'is_active']
    list_filter = ['role']
    search_fields = ['username', 'email']

    def has_view_permission(self, request, obj=None):
        if not request.user.is_authenticated:
            return False
        if request.user.is_custom_superuser():
            return True
        if request.user.role == 'admin':
            return True
        return False

    def has_add_permission(self, request):
        if not request.user.is_authenticated:
            return False
        if request.user.is_custom_superuser():
            return True
        if request.user.role == 'admin':
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if not request.user.is_authenticated:
            return False
        if request.user.is_custom_superuser():
            return True
        if request.user.role == 'admin':
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_authenticated:
            return False
        if request.user.is_custom_superuser():
            return True
        if request.user.role == 'admin':
            return False
        return False

    def get_queryset(self, request):
        if not request.user.is_authenticated:
            return self.model.objects.none()
        qs = super().get_queryset(request)
        if request.user.is_custom_superuser():
            return qs.filter(role='admin')  # Superusers can only see admin users
        if request.user.role == 'admin':
            return qs.filter(role__in=['agent', 'validator', 'account'])  # Admins can see agents, validators, and accounts
        return qs.none()

    def save_model(self, request, obj, form, change):
        if request.user.is_authenticated:
            if request.user.is_custom_superuser() and not change:
                obj.role = 'admin'
                obj.is_staff = True
                obj.is_superadmin = True
            elif request.user.role == 'admin' and not change:
                if 'agent' in request.POST:
                    obj.role = 'agent'
                elif 'validator' in request.POST:
                    obj.role = 'validator'
                elif 'account' in request.POST:
                    obj.role = 'account'
                obj.is_staff = False 
        super().save_model(request, obj, form, change)


admin.site.register(User, CustomUserAdmin)

class FormAdmin(admin.ModelAdmin):
    list_display = ['id', 'agent', 'validator', 'company', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'company']
    search_fields = ['agent__username', 'validator__username', 'company__name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'admin':
            # Restrict Admins to see only forms related to their company (modify this logic as needed)
            return qs.filter(company__name=request.user.company.name)
        return qs

    def save_model(self, request, obj, form, change):
        if request.user.role == 'admin':
            if obj.agent.role != 'agent' or obj.validator.role != 'validator':
                raise ValidationError("Only Agents and Validators can be assigned to forms.")
            if obj.validator and obj.status != 'pending':
                raise ValidationError("Only pending forms can be assigned to a validator.")
        super().save_model(request, obj, form, change)



admin.site.register(Form, FormAdmin)
