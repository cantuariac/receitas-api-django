from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from authentication.models import User
from recipes.models import Recipe

class RecipeCRUDTest(TestCase):
    def setUp(self):
        self.chef_carmen = User.objects.create_user(username='carmen', password='1q2w3e', role='chef')
        self.chef_sydney = User.objects.create_user(username='sydney', password='1q2w3e', role='chef')
        self.reader_user = User.objects.create_user(username='claire', password='1q2w3e', role='reader')
        self.recipe_carmen = Recipe.objects.create(author=self.chef_carmen, name='test recipe carmen', description='', ingredients='', directions='')
        self.recipe_sydney = Recipe.objects.create(author=self.chef_sydney, name='test recipe sydney', description='', ingredients='', directions='')

        self.client = APIClient()

    def test_only_chef_can_create_recipe(self):
        recipe_data = {
                "name": "Bolo de banana",
                "description": "Bolo de banana",
                "ingredients": "1 banana,1 X farinha de trigo",
                "directions": "amasse a banana\nmisture o trigo"
            }
        user_token = Token.objects.create(user=self.reader_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.key)
        response = self.client.post("/recipes/create/",data=recipe_data)
        self.assertContains(response, text='', status_code=status.HTTP_403_FORBIDDEN)
        
        user_token = Token.objects.create(user=self.chef_sydney)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.key)
        response = self.client.post("/recipes/create/",data=recipe_data)
        self.assertContains(response, text='', status_code=status.HTTP_201_CREATED)
        
    def test_only_author_can_edit_recipe(self):
        user_token = Token.objects.create(user=self.chef_carmen)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.key)
        response = self.client.get(f"/recipes/{self.recipe_sydney.id}/edit/")
        self.assertContains(response, text='', status_code=status.HTTP_403_FORBIDDEN)
        
        user_token = Token.objects.create(user=self.chef_sydney)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user_token.key)
        response = self.client.get(f"/recipes/{self.recipe_sydney.id}/edit/")
        self.assertContains(response, text='', status_code=status.HTTP_200_OK)

