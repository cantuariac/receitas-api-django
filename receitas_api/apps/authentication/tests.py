from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from authentication.models import User

class AuthenticateUserTest(TestCase):
    def setUp(self):
        self.chef_user = User.objects.create_user(username='test_chef', password='1q2w3e', role='chef')
        
        self.client = APIClient()

    def test_user_not_authenticated(self):
        response = self.client.get("/auth/")
        self.assertContains(response, "Authentication credentials were not provided.", status_code=status.HTTP_401_UNAUTHORIZED)
        
        user_token = Token.objects.create(user=self.chef_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.key)
        response = self.client.get("/auth/")
        self.assertContains(response, "", status_code=status.HTTP_200_OK)
