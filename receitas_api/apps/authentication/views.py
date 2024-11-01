from django.shortcuts import render
from django.conf import settings

from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

from authentication.models import User
from authentication.serializers import UserSerializer

class RegisterUser(CreateAPIView):
    """End point para registro de usuário de API
    """
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserProfile(GenericAPIView):
    """Detalhes do usuário autenticado
    """
    permission_classes = [IsAuthenticated]
    serializer_class=UserSerializer
    def get(self, request, format=None):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class ObtainUserAuthToken(ObtainAuthToken):
    """Endpoint para obter Token de autenticação de usuário
    Para utilizar o token adicione o seguinte header à suas requisições: Authorization: Token [token]
    """