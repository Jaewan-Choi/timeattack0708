from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, SignInView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView # JWT refresh 토큰 발급 view 인증토큰을 재발급받기위한 또 다른 토큰 
from user.views import OnlyAuthenticatedUserView

urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    path('sign-in', SignInView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/authonly/', OnlyAuthenticatedUserView.as_view()),
]
