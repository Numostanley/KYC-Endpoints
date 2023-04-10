from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, RegistrationSerializer

# Create your views here.

class UserRegister(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    

class UserDataAPI(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer =  UserSerializer(user)
        return Response(serializer.data)
    
class RegisterAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    