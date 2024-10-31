from django.urls import path

from recipes.views import ListRecipes, ListRecipesByAuthor, RetrieveRecipe, CreateRecipe, RetrieveUpdateDestroyRecipe, ListChefs

urlpatterns = [
    path('', ListRecipes.as_view()),
    path('author/<int:author_id>/', ListRecipesByAuthor.as_view()),
    path('<int:pk>/', RetrieveRecipe.as_view()),
    path('create/', CreateRecipe.as_view()),
    path('<int:pk>/edit/', RetrieveUpdateDestroyRecipe.as_view()),
    path('chefs/', ListChefs.as_view()),
]