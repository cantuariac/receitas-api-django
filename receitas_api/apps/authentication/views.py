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

class HelloUser(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        request.user.username
        return Response("Hello " + request.user.username)

class HelloChef(GenericAPIView):
    permission_classes = [IsAuthenticated, IsChef]
    def get(self, request, format=None):
        request.user.username
        return Response("Hello chef " + request.user.username)
