from django.shortcuts import render
from django.conf import settings

from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from authentication.models import User
from authentication.serializers import UserSerializer
from authentication.permissions import IsChef

class RegisterUser(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserProfile(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class=UserSerializer
    def get(self, request, format=None):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
