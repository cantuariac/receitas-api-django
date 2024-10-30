from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import permissions, authentication
from rest_framework.response import Response

from .serializers import UserSerializer

class RegisterUser(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class HelloUser(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]
    def get(self, request, format=None):
        request.user.username
        return Response("Hello " + request.user.username)

# from django.contrib.auth.models import Group
# def populate_groups():
#     Group.objects.all()