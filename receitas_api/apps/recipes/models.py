from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Recipe(models.Model):
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=50)
    description = models.CharField("Descrição", max_length=150)
    ingredients = models.TextField("Ingredientes")
    directions = models.TextField("Modo de preparo")