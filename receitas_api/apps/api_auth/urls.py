from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterUser, HelloUser

urlpatterns = [
    path('token/', obtain_auth_token),
    
    path('register/', RegisterUser.as_view()),
    path("", HelloUser.as_view())
]