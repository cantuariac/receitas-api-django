from django.urls import path, include

from rest_framework.authtoken.views import ObtainAuthToken

from authentication.views import RegisterUser, UserProfile

urlpatterns = [
    path("", include('rest_framework.urls')),
    path("", UserProfile.as_view()),
    path('token/', ObtainAuthToken.as_view()),
    path('register/', RegisterUser.as_view()),
]