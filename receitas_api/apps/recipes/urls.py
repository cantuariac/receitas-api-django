from django.urls import path

from recipes.views import ListRecipes, RetrieveRecipe, CreateRecipe, RetrieveUpdateDestroyRecipe

urlpatterns = [
    path('', ListRecipes.as_view()),
    path('<int:pk>/', RetrieveRecipe.as_view()),
    path('create/', CreateRecipe.as_view()),
    path('<int:pk>/edit/', RetrieveUpdateDestroyRecipe.as_view()),
]