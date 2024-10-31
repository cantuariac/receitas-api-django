from django.shortcuts import render
from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.request import Request

from authentication.permissions import IsChef
from authentication.serializers import UserSerializer
from authentication.models import User

from recipes.permissions import IsRecipesAuthor
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

class ListRecipes(ListAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Recipe.objects.all()
        params = self.request.query_params
        query = Q()
        if 'q' in params:
            query |= Q(name__icontains=params['q']) | Q(description__icontains=params['q'])
        if 'recipe_name' in params:
            query |= Q(name__icontains=params['recipe_name'])
        if 'author_name' in params:
            query |= Q(author__username=params['author_name'])
        
        return queryset.filter(query)

class ListRecipesByAuthor(ListRecipes):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs['author_id']
        return queryset.filter(author_id=author_id)

class RetrieveRecipe(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

class CreateRecipe(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated, IsChef]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RetrieveUpdateDestroyRecipe(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated, IsChef, IsRecipesAuthor]

class ListChefs(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.all().filter(role='chef')
    
