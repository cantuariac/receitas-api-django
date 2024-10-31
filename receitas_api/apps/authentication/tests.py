from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from authentication.models import User

class AuthenticateUserTest(TestCase):
    def setUp(self):
        chef_user = User.objects.create_user(username='test_chef', password='1q2w3e', role='chef')
        chef_token = Token.objects.create(user=chef_user)

        self.client = APIClient()
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + chef_token.key)

    def test_user_not_authenticated(self):
        response = self.client.get("/auth/")

        self.assertContains(response, "Authentication credentials were not provided.", status_code=401)
