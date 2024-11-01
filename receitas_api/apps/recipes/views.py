from django.shortcuts import render
from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from authentication.permissions import IsChef
from authentication.serializers import UserSerializer
from authentication.models import User

from recipes.permissions import IsRecipesAuthor
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

q = openapi.Parameter('q', openapi.IN_QUERY,
                        description="Termo de pesquisa",
                        type=openapi.TYPE_STRING)
recipe_name = openapi.Parameter('recipe_name', openapi.IN_QUERY,
                        description="Pesquisa por nome de receita",
                        type=openapi.TYPE_STRING)
author_name = openapi.Parameter('author_name', openapi.IN_QUERY,
                        description="Pesquisa por nome de autor ",
                        type=openapi.TYPE_STRING)

class ListRecipes(ListAPIView):
    """Lista de receitas cadastradas
    Contem filtros de busca
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(manual_parameters=[q, recipe_name, author_name])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
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
    """Lista de receitas cadastradas por um autor
    Contem filtros de busca
    """
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs['author_id']
        return queryset.filter(author_id=author_id)

class RetrieveRecipe(RetrieveAPIView):
    """Detalhes de uma receita
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

class CreateRecipe(CreateAPIView):
    """Endpoint para cadastro de uma receita
    Somente usuários com função 'chef' podem cadastrar receitas
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated, IsChef]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RetrieveUpdateDestroyRecipe(RetrieveUpdateDestroyAPIView):
    """Endpoint para edição e remoção de uma receita
    Usuários só podem editar receitas das quais são autores
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated, IsChef, IsRecipesAuthor]

class ListChefs(ListAPIView):
    """Lista de usuário com função 'chef'
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.all().filter(role='chef')
    
