from django.urls import path, include

from authentication.views import RegisterUser, UserProfile, ObtainUserAuthToken

urlpatterns = [
    path("", include('rest_framework.urls')),
    path("", UserProfile.as_view()),
    path('register/', RegisterUser.as_view()),
    path('token/', ObtainUserAuthToken.as_view()),
]