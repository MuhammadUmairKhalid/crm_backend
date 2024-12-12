from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'role', 'is_active', 'is_staff']
    search_fields = ['username', 'role']
    list_filter = ['role', 'is_active', 'is_staff']

    def save_model(self, request, obj, form, change):
        """
        Override save_model to hash the password if it's being changed.
        """
        if form.cleaned_data.get("password") and not obj.password.startswith("pbkdf2_"):
            obj.set_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)

