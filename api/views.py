from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from api.permissions import IsAgent
from dashboard.models import User
from rest_framework import status
from django.contrib.auth.hashers import check_password
class Login(APIView):
    authentication_classes = [] 
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        user_name = request.data.get("user_name")
        password = request.data.get("password")

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
    

class AddFormData(APIView):
    authentication_classes = [TokenAuthentication,] 
    permission_classes = [IsAuthenticated,IsAgent]
    throttle_classes = [AnonRateThrottle]

    def post(self, request):
        
        return Response(
            {"status": "success"},
            status=status.HTTP_200_OK
        )
