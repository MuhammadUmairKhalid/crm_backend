from rest_framework import serializers
from dashboard.models import Company, Form
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

class FormSerializer(serializers.ModelSerializer):
    initial_draft_date = serializers.DateField(input_formats=["%Y-%m-%d"])
    dob = serializers.DateField(input_formats=["%Y-%m-%d"])
    class Meta:
        model = Form
        fields ='__all__'
    def validate(self, data):
        # Custom validation logic if required
        if data['agent'].role != 'agent':
            raise serializers.ValidationError("User must have the 'agent' role.")
        return data
    

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not check_password(value, user.password):
            raise serializers.ValidationError("Old password is incorrect.")
        return value

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("New password must be at least 8 characters long.")
        return value