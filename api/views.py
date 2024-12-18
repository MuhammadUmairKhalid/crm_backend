from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework import viewsets
import json
from api.permissions import IsAgent,IsValidator
from dashboard.models import User
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .serializers import CompanySerializer, FormSerializer
from dashboard.models import Form,Company
class Login(APIView):
    authentication_classes = [] 
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        user_name = request.data.get("user_name")
        password = request.data.get("password")
        print(user_name,password)
        if not user_name or not password:
            return Response(
                {"status": "username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            return Response(
                {"status": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not check_password(password, user.password):
            return Response(
                {"status": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {"status": "success", "token": str(token),"role":user.role},
            status=status.HTTP_200_OK
        )
    
class FormDataViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAgent]
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def create(self, request, *args, **kwargs):
        form_data = request.data['form']
        if form_data["initial_draft_date"]=='' and form_data["dob"]=='':
            return Response(
                {"status": "error", "errors": "Both initial_draft_date and dob cannot be provided"},
            )
        company_name = form_data['insurance_company']
        company = Company.objects.filter(name=company_name).first()
        if company is None:
            obj = Company.objects.create(name=company_name,bonus_formula="2+3/5")
            obj.save()
            company_serializer = CompanySerializer(data=obj)
            if company_serializer.is_valid():
                company = company_serializer.save()
            else:
                return Response(
                    {"status": "error", "errors": company_serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        form_data['company'] = company.id
        form_data['agent'] = request.user.id 
        print(company.id)
        print(request.user.id)
        print(form_data['initial_draft_date'])
        print(form_data['dob'])
        print(type(form_data['initial_draft_date']))
        print(type(form_data['dob']))
        form_serializer = FormSerializer(data=form_data)
        if form_serializer.is_valid():
            form_serializer.save()
            return Response(
                {"status": "success", "data": form_serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            print(form_serializer.errors)
            return Response(
                {"status": "error", "errors": form_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, *args, **kwargs):
        return Response(
                {"status": "error","messgae":"You cannot delete a form"},
                status=status.HTTP_400_BAD_REQUEST
            )
    def update(self, request, *args, **kwargs):
        return Response(
                {"status": "error","messgae":"You cannot update a form"},
                status=status.HTTP_400_BAD_REQUEST
            )
    

class validatorformViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsValidator]  # Assuming `IsValidator` is a custom permission class
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def list(self, request, *args, **kwargs):
        try:
            pending_forms = Form.objects.filter(status="pending")
    
            serializer = self.get_serializer(pending_forms, many=True)
            
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )