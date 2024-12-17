from rest_framework import serializers
from dashboard.models import Company, Form
from django.contrib.auth import get_user_model

User = get_user_model()

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'bonus_formula']

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields ='__all__'
    def validate(self, data):
        # Custom validation logic if required
        if data['agent'].role != 'agent':
            raise serializers.ValidationError("User must have the 'agent' role.")
        return data