from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from authentication.views import RegisterUser, HelloUser, HelloChef

urlpatterns = [
    path('token/', ObtainAuthToken.as_view()),
    
    path('register/', RegisterUser.as_view()),
    path("", HelloUser.as_view()),
    path("chef", HelloChef.as_view())
]