from rest_framework.request import Request

from authentication.permissions import IsChef
from recipes.models import Recipe

class IsRecipesAuthor(IsChef):
    def has_object_permission(self, request:Request, view, obj:Recipe):
        return request.user == obj.author